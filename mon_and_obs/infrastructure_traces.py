from diagrams import Cluster, Diagram

from diagrams.k8s.infra import Node

from diagrams.azure.compute import KubernetesServices

from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.tracing import Tempo
from diagrams.onprem.monitoring import Grafana

from diagrams.custom import Custom

from diagrams.azure.general import Helpsupport

with Diagram("Infrastructure Architecture >> Observability Traces System", direction="LR", filename="mon_and_obs_infrastucture_traces", show=False):

    with Cluster("Control Plane"):
      aks = KubernetesServices("AKS")

    with Cluster("Node Pool Metrics"):
      
      node_t01 = Node("NODE T01")
      node_t02 = Node("NODE T02")
      node_t03 = Node("NODE T03")
      nodes_t = [node_t01, node_t02, node_t03]

    with Cluster("NODE T01 | Standard_B4s_v2 | Rafagas"):
      aks_node_t01  = KubernetesServices("Node T01​")
      tempo_t01     = Tempo("tempo")
      grafana_t01   = Grafana("Grafana")

    with Cluster("NODE T02 | Standard_B4s_v2 | Rafagas"):
      aks_node_t02  = KubernetesServices("Node T02​")
      tempo_t02     = Tempo("tempo")
      grafana_t02   = Grafana("Grafana")

    with Cluster("NODE T03 | Standard_B4s_v2 | Rafagas"):
      aks_node_t03  = KubernetesServices("Node T03​")
      tempo_t03     = Tempo("tempo")
      grafana_t03   = Grafana("Grafana")
    
    fluentbit = Fluentd("Fluentbit")
    users     = Helpsupport()

    # Cluster
    aks >> nodes_t
    
    # Node 01
    node_t01 >> aks_node_t01
    tempo_t01 << grafana_t01
    
    # Node 02
    node_t02 >> aks_node_t02
    tempo_t02 << grafana_t02
    
    # Node 03
    node_t03 >> aks_node_t03
    tempo_t03 << grafana_t03

    # Logs Collector
    Custom("APP Traces", "./assets/img/apps-logo.png") >> fluentbit 
    fluentbit >> [tempo_t01, tempo_t02, tempo_t03]

    # Helpsupport
    [grafana_t01, grafana_t02, grafana_t03] << users
