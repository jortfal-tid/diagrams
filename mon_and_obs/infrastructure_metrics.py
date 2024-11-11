from diagrams import Cluster, Diagram

from diagrams.k8s.infra import Node
from diagrams.k8s.storage import PV
from diagrams.k8s.compute import Pod

from diagrams.azure.compute import KubernetesServices

from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.monitoring import Thanos
from diagrams.onprem.monitoring import Grafana

from diagrams.azure.general import Helpsupport

with Diagram("Monitoring and observability System Infrastructure Architecture", show=False):

    with Cluster("Control Plane"):
      aks = KubernetesServices("AKS")

    with Cluster("Nodes"):
      
      node_01 = Node("Node 01")
      node_02 = Node("Node 02")
      node_03 = Node("Node 03")
      nodes = [node_01, node_02, node_03]

    with Cluster(""):
      aks_node_01            = KubernetesServices("Node 01")
      ssd_01                 = PV("SSD")
      k8s_metrics_01         = Pod("kube-state-metrics")
      prometheus_exporter_01 = Pod("prometheus-node-exporter")
      prometheus_01          = Prometheus("Prometheus")
      thanos_01              = Thanos("Thanos")
      grafana_01             = Grafana("Grafana")

    with Cluster("Node 02"):
      aks_node_02            = KubernetesServices("Node 02")
      ssd_02                 = PV("SSD")
      k8s_metrics_02         = Pod("kube-state-metrics")
      prometheus_exporter_02 = Pod("prometheus-node-exporter")
      prometheus_02          = Prometheus("Prometheus")
      thanos_02              = Thanos("Thanos")
      grafana_02             = Grafana("Grafana")

    with Cluster("Node 03"):
      aks_node_03            = KubernetesServices("Node 03")
      ssd_03                 = PV("SSD")
      k8s_metrics_03         = Pod("kube-state-metrics")
      prometheus_exporter_03 = Pod("prometheus-node-exporter")
      prometheus_03          = Prometheus("Prometheus")
      thanos_03              = Thanos("Thanos")
      grafana_03             = Grafana("Grafana")
    
    users = Helpsupport()

    # AKS
    aks >> nodes
    grafana_01 << users
    grafana_02 << users
    grafana_03 << users
    # Node 01
    node_01 >> aks_node_01
    k8s_metrics_01 << prometheus_exporter_01
    prometheus_exporter_01 << prometheus_01
    ssd_01 << prometheus_01
    prometheus_01 << grafana_01
    ssd_01 >> thanos_01
    thanos_01 << grafana_01
    # Node 02
    node_02 >> aks_node_02
    k8s_metrics_02 << prometheus_exporter_02
    prometheus_exporter_02 << prometheus_02
    ssd_02 << prometheus_02
    prometheus_02 << grafana_02
    ssd_02 >> thanos_02
    thanos_02 << grafana_02
    # Node 03
    node_03 >> aks_node_03
    k8s_metrics_03 << prometheus_exporter_03
    prometheus_exporter_03 << prometheus_03
    ssd_03 << prometheus_03
    prometheus_03 << grafana_03
    ssd_03 >> thanos_03
    thanos_03 << grafana_03