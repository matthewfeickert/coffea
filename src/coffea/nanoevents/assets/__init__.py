import os
import yaml
from functools import partial


root_dir = os.path.dirname(os.path.abspath(__file__))

versions  = [
    "00-10-01",
    "00-10-02",
    "00-10-03",
    "00-10-04",
    "00-10-05",
    "00-99-00",
    "00-99-01",
]

def _load_edm4hep_version(yamlfile):
    with open(yamlfile, 'r') as f:
        loaded = yaml.safe_load(f)
    return loaded

edm4hep_ver  = {
    version: partial(
        _load_edm4hep_version,
        yamlfile=os.path.join(root_dir, f"edm4hep_v{version}.yaml")
    )
    for version in versions
}
