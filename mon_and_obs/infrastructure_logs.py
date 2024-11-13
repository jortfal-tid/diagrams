from diagrams import Cluster, Diagram

from diagrams.k8s.infra import Node

from diagrams.azure.compute import KubernetesServices
from diagrams.azure.storage import StorageAccounts

from diagrams.onprem.aggregator import Fluentd
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.elastic.elasticsearch import Kibana

from diagrams.generic.compute import Rack
from diagrams.custom import Custom

from diagrams.azure.general import Helpsupport

with Diagram("Infrastructure Architecture >> Monitoring Logs System", direction="TB", filename="mon_and_obs_infrastucture_logs", show=False):

    with Cluster("Control Plane"):
      aks = KubernetesServices("AKS")

    with Cluster("Node Pool Logs"):
      
      node_l01 = Node("NODE L01")
      node_l02 = Node("NODE L02")
      node_l03 = Node("NODE L03")

      nodes_m = [node_l01, node_l02, node_l03]

    with Cluster("NODE L01 | Standard_B4s_v2 | Rafagas"):

      aks_node_l01            = KubernetesServices("Node L01​")
      az_storage_account_01  = StorageAccounts("Storage Account")
      elasticsearch_01       = Elasticsearch("Elasticsearch")
      Kibana_01              = Kibana("Kibana")

    with Cluster("NODE L02 | Standard_B4s_v2 | Rafagas"):

      aks_node_l02           = KubernetesServices("Node L02​")
      az_storage_account_02  = StorageAccounts("Storage Account")
      elasticsearch_02       = Elasticsearch("Elasticsearch")
      Kibana_02              = Kibana("Kibana")

    with Cluster("NODE L03 | Standard_B4s_v2 | Rafagas"):

      aks_node_l03           = KubernetesServices("Node L03​")
      az_storage_account_03  = StorageAccounts("Storage Account")
      elasticsearch_03       = Elasticsearch("Elasticsearch")
      Kibana_03              = Kibana("Kibana")
    
    fluentbit = Fluentd("Fluentbit")
    users     = Helpsupport()

    # Cluster
    aks >> nodes_m

    # Node L01
    node_l01 >> aks_node_l01
    az_storage_account_01 << elasticsearch_01 << Kibana_01

    # Node L02
    node_l02 >> aks_node_l02
    az_storage_account_02 << elasticsearch_02 << Kibana_02

    # Node L03
    node_l03 >> aks_node_l03
    az_storage_account_03 << elasticsearch_03 << Kibana_03
    
    # Logs Collector
    Custom("APPs", "./assets/img/apps-logo.png") >> fluentbit 
    Rack("Systems") >> fluentbit 
    fluentbit >> [elasticsearch_01, elasticsearch_02, elasticsearch_03]

    # Helpsupport
    [Kibana_01, Kibana_02, Kibana_03] << users