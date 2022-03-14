# data-manager-job-callback-server
A basic Data Manager Job Callback Server, that can be used
as a dummy receiver of callbacks from the Data Manager.

    $ docker-compose build
    $ docker-compose up -d

## Deployment (kubernetes)
Assuming you have a namespace (like `data-manager-job-callback-server`)
you can deploy the simple server using the kubernetes object files in
the `kubernetes` directory: -

    $ kubectl config set-context --current \
        --namespace=data-manager-job-callback-server

    $ pushd kubernetes
    $ kubectl create -f deployment.yaml
    $ kubectl create -f service.yaml
    $ popd

The callback server can then be used from a Data Manager in the same
cluster using the callback URL that's based on the service name
and namespace. For this example the Job callback URL will be: -

    http://callback-server.data-manager-job-callback-server:8080/job-callback

---
