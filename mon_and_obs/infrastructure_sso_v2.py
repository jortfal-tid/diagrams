from diagrams import Cluster, Diagram

from diagrams.k8s.infra import Node

from diagrams.azure.compute import KubernetesServices

from diagrams.onprem.monitoring import Prometheus
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.onprem.tracing import Tempo
from diagrams.custom import Custom

from diagrams.oci.security import Vault

from diagrams.azure.general import Helpsupport

with Diagram("How will the Access and Security of the Tools be? >> SSO & 2FA Latch", direction="TB", filename="mon_and_obs_infrastucture_latch", show=False):

    with Cluster("Control Plane"):
      aks = KubernetesServices("AKS")

    with Cluster("Node Pool K8S"):
      
      node_pool_s = KubernetesServices()

    with Cluster("Node Pool Metrics"):
      
      node_pool_m = Prometheus()

    with Cluster("Node Pool Logs"):
 
      node_pool_l = Elasticsearch()

    with Cluster("Node Pool Traces"):
        
      node_pool_t = Tempo()

    with Cluster("Node Pool AI"):

      node_pool_ai = Custom("", "./assets/img/ai-logo.png")
    
    # Cluster
    aks >> [node_pool_s, node_pool_m, node_pool_l, node_pool_t, node_pool_ai]

    sso       = Vault("SSO")
    latch     = Custom("", "./assets/img/latch-logo.png")
    users     = Helpsupport()
    [node_pool_m, node_pool_l, node_pool_t, node_pool_ai] << latch << sso << users
