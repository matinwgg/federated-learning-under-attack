# Federated Learning Under Attack

## 📖 About

A research project studying the robustness of federated-learning systems when clients or training updates are adversarial. It focuses on the interaction between aggregation algorithms, poisoning behavior, and model performance.

## 🎯 Why It Exists

Federated learning changes the trust boundary: a central server may receive model updates from participants it cannot fully trust. This project investigates how adversarial clients can influence aggregation and how robust methods respond.

## ✨ Planned Features

- Malicious-client simulation
- Data and model poisoning
- Byzantine update generation
- FedAvg baselines
- Robust aggregation comparisons
- Attack-success and accuracy metrics
- Repeated-trial experiments

## 🛠 Tech Stack

- Python
- NumPy
- ML framework selected by experiments
- Statistical evaluation tooling

## 🏗 Architecture

```text
Federated clients
   ├── benign updates
   └── adversarial updates
            ↓
       Server aggregator
            ↓
        Global model
            ↓
   Clean + adversarial evaluation
```

## 📁 Project Structure

Currently a scaffold. Future implementation should separate client simulation, attack generation, aggregators, evaluation, and experiment configuration.

## 📋 Prerequisites

No runnable implementation is currently documented.

## 🚀 Getting Started

```bash
git clone https://github.com/matinwgg/federated-learning-under-attack.git
cd federated-learning-under-attack
```

## 🧮 Mathematical Foundations

The work uses vector aggregation, norms, robust statistics, optimization, probability, influence, concentration behavior, and statistical uncertainty.

## 🧪 Evaluation

Report clean accuracy, attack success, robust accuracy, client corruption rate, aggregation parameters, repeated-trial variability, and computational cost.

## 🔐 Security Scope

Experiments should use controlled models/datasets. Research results must state the attacker capabilities and aggregation assumptions explicitly.

## 🚧 Future Work

- Adaptive attackers
- Byzantine-robust aggregation
- Secure aggregation interaction studies
- Differential privacy interaction studies
- Large-scale reproducible benchmarks

## 🤝 Contributing

Document threat models, attack parameters, aggregation assumptions, and reproducibility details.

## 📄 License

See repository license information.

## 👨‍💻 Author

**Matin Odoom**
