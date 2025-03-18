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
      
      node_pool_s = KubernetesServices("Standard_B2s_v2​")
      node_s01    = Node("Node S01")
      node_s02    = Node("Node S02")
      node_s03    = Node("Node S03")
      
      node_pool_s >> [node_s01, node_s02, node_s03]
      
      aks_node_pool_s = [node_s01, node_s02, node_s03]

    with Cluster("Node Pool Metrics"):
      
      node_pool_m = Prometheus("Standard_B4s_v2")

      node_m01    = Node("Node M01")
      node_m02    = Node("Node M02")
      node_m03    = Node("Node M03")

      node_pool_m >> [node_m01, node_m02, node_m03]

      aks_node_pool_m = [node_m01, node_m02, node_m03]

    with Cluster("Node Pool Logs"):
 
      node_pool_l = Elasticsearch("Standard_D4_v5")

      node_l01    = Node("Node L01")
      node_l02    = Node("Node L02")
      node_l03    = Node("Node L03")

      node_pool_l >> [node_l01, node_l02, node_l03]

      aks_node_pool_l = [node_l01, node_l02, node_l03]

    with Cluster("Node Pool Traces"):
        
      node_pool_t = Tempo("Standard_B4s_v2")

      node_t01    = Node("Node T01")
      node_t02    = Node("Node T02")
      node_t03    = Node("Node T03")

      node_pool_t >> [node_t01, node_t02, node_t03]

    with Cluster("Node Pool AI"):

      node_pool_ai = Custom("Standard_NC16as_T4_v3", "./assets/img/ai-logo.png")

      node_ai01 = Node("Node AI01")
      node_ai02 = Node("Node AI02")

      node_pool_ai >> [node_ai01, node_ai02]
    
    # Cluster
    aks >> [node_pool_s, node_pool_m, node_pool_l, node_pool_t, node_pool_ai]

    sso       = Vault("SSO")
    latch     = Custom("", "./assets/img/latch-logo.png")
    users     = Helpsupport()
    [node_pool_m, node_pool_l, node_pool_t, node_pool_ai] << latch << sso << users
