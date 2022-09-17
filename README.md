# squonk2-data-manager-job-callback-server
A basic Python/Flask application (in a compact container image)
that can be used as target for Data Manager _Job Callbacks_. It exposes
a **PUT** endpoint at `/job-callback` that responds with a `200` and
dumps the received JSON payload to stdout.

    $ docker-compose build
    $ docker-compose up -d

## Deployment (kubernetes)
Assuming you have a **Namespace** (like `data-manager-job-callback-server`)
you can deploy the simple server using `kubectl` and the kubernetes object
files in  the `kubernetes` directory.

>   For the files in this repository you will need a **Pod Security Policy**
    called `im-core-unrestricted` with sufficient ability to deploy Pods
    within the chosen namespace (Our PSP, as the name suggests, is a lot more
    capable).

    $ kubectl create -f kubernetes/objects.yaml \
        -n data-manager-job-callback-server

The callback server can then be used from a Data Manager in the same
cluster using a callback URL that's based on the **Service** name
and **Namespace**. For this example the Job callback URL will be: -

    http://callback-server.data-manager-job-callback-server:8080/job-callback

And, from a shell in the Data Manager API Pod (for example)
you should be able to test the connection to the callback server using _curl_:-

    curl -X PUT -d '{"param1":1}' \
        http://callback-server.data-manager-job-callback-server:8080/job-callback 

...or Python: -

    python
    >>> import requests
    >>> url = 'http://callback-server.data-manager-job-callback-server:8080/job-callback'
    >>> requests.put(url, json={"param1":1})
    <Response [200]>

To remove the callback server either remove the namespace it's in or
use `kubectl` to reverse the actions: -

    $ kubectl delete -f kubernetes/objects.yaml \
        -n data-manager-job-callback-server

---
