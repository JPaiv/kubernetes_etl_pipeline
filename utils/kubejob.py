import sys
import json
import logging
import kubernetes.client as clt
from kubernetes import config
from kubernetes.client.rest import ApiException


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def create_kube_job(name, kube_args, index, requests=None, limits=None):
    index = str(index)

    if '_' in name:
        name = name.replace('_', '-')

    try:
        config.load_incluster_config() # Inside cluster job creation
    except Exception:
        config.load_kube_config()
    env_list = [
        clt.V1EnvVar(
            **{
                "name": "A",
                "value_from": clt.V1EnvVarSource(
                    **{
                        "secret_key_ref": clt.V1SecretKeySelector(
                            **{
                                "name": "",
                                "key": "",
                            }
                        )
                    }
                ),
            }
        ),

        clt.V1EnvVar(
            **{
                "name": "A",
                "value_from": clt.V1EnvVarSource(
                    **{
                        "secret_key_ref": clt.V1SecretKeySelector(
                            **{
                                "name": "",
                                "key": "AY",
                            }
                        )
                    }
                ),
            }
        ),
    ]

    if not limits or not isinstance(limits, dict):
        limits = {"cpu": "1",
                  "memory": '1500Mi'}
    if not requests or not isinstance(requests, dict):
        requests = {"cpu": "0.5",
                    "memory": '500Mi'}

    # Define docker container run by job, its params and computational resources
    container = clt.V1Container(
        name=",
        image=",
        command=['python3'],
        args=kube_args,
        resources=clt.V1ResourceRequirements(
            limits=limits,
            requests=requests
        ),
        env=env_list,
    )
    # Define Pod running the job; use spot price since it is cheaper
    pod_spec = clt.V1PodSpec(
        containers=[container],
        restart_policy="Never",
        priority_class_name="batch-low",
        image_pull_secrets=[clt.V1LocalObjectReference(
            name=name + '-node')],
        affinity=clt.V1Affinity(
            node_affinity=clt.V1NodeAffinity(
                required_during_scheduling_ignored_during_execution=clt.V1NodeSelector(
                    node_selector_terms=[
                        clt.V1NodeSelectorTerm(
                            match_expressions=[
                                clt.V1NodeSelectorRequirement(
                                    key="awstype", operator="In", values=["spot"]
                                )
                            ]
                        )
                    ]
                )
            )
        ),
    )

    # Give job an unique name and define app
    metadata = clt.V1ObjectMeta(
        name=name + '-job-' + str(index), labels={"app": name
    )

    # Bring it all together by defining the whole job
    job = clt.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=metadata,
        spec=clt.V1JobSpec(
            template=clt.V1PodTemplateSpec(metadata=metadata, spec=pod_spec)
        ),
    )
    # Create an instance of the API class
    api_instance = clt.BatchV1Api()
    namespace = "default"
    try:
        api_response = api_instance.create_namespaced_job(namespace, job)
        logging.info("Created %s", api_response.metadata.name)
    except ApiException as e:
        logging.info(json.loads(e.body)["message"])
        logging.info("Exception when calling BatchV1Api->create_namespaced_job: %s", e)
        return False
