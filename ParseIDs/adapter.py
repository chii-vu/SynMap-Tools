import re
from pathlib import Path

"""
This adapter is used to parse the ids from the query and subject file names.
The query and subject file names are expected to be in the format:
    <query_name>_<subject_name>_<query_id>_<subject_id>.<ext>
"""
def parse_ids(context, *args, **kwargs):
    param_index, query, fs = context.getdataarg(0, 'query', *args, **kwargs)
    _, subject, _ = context.getdataarg(param_index, 'subject', *args, **kwargs)
    
    query_stem = Path(query).stem
    subject_stem = Path(subject).stem

    ids = re.findall(r'\d+', query_stem + subject_stem)
    
    return str(ids[0]), str(ids[1])
