from diagrams import Cluster, Diagram

from diagrams.k8s.infra import Node

from diagrams.azure.compute import KubernetesServices

from diagrams.generic.blank import Blank
from diagrams.custom import Custom


with Diagram("Infrastructure Architecture >> AI to Observability", direction="TB", filename="mon_and_obs_infrastucture_ai", show=False):
    
    with Cluster("Control Plane"):
      aks = KubernetesServices("AKS")

    with Cluster("Node Pool AI"):
      
      node_ai01 = Node("NODE AI01")
      node_ai02 = Node("NODE AI02")

      nodes_ai = [node_ai01, node_ai02]

    with Cluster("NODE AI01 | Standard_NC16as_T4_v3​"):

      aks_node_ai01 = KubernetesServices("Node AI01​")
      ai_01 = Custom("AI Models", "./assets/img/ai-logo.png")

    with Cluster("NODE AI02 | Standard_NC16as_T4_v3​"):

      aks_node_ai02 = KubernetesServices("Node AI02​")
      ai_02 = Custom("AI Models", "./assets/img/ai-logo.png")


    # Cluster
    aks >> nodes_ai

    # Node AI01
    node_ai01 >> aks_node_ai01

    # Node AI02
    node_ai02 >> aks_node_ai02

