# k8sv1
Kubernetes API v1 python client

To genearate a new version:


download the latest swagger spec (currently living at https://github.com/kubernetes/kubernetes/blob/master/api/swagger-spec/v1.json)

Install https://github.com/swagger-api/swagger-codegen


run:

swagger-codegen generate -l python -o k8sv1 -i v1.json -c v1_config.json


to install:

python setup install
python setup install_lib
