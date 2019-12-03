def remove_empty_values(prospect):
    return {k:v for k, v in prospect.items() if v}
