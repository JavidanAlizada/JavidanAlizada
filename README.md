<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Javidan Alizada: Senior Software Engineer, distributed, high-concurrency, low-latency systems in Java" src="assets/banner-dark.svg" width="100%">
</picture>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/javidan-alizada-284781153/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:javidanalizada99@gmail.com)

</div>

<table align="center">
  <tr>
    <td align="center" width="150"><h2>300×</h2><sub>platform scalability</sub></td>
    <td align="center" width="150"><h2>100K</h2><sub>concurrent clients</sub></td>
    <td align="center" width="150"><h2>~85%</h2><sub>faster troubleshooting</sub></td>
    <td align="center" width="150"><h2>~150%</h2><sub>performance gain</sub></td>
    <td align="center" width="150"><h2>8+</h2><sub>years in production</sub></td>
  </tr>
</table>

## 👨‍💻 About Me

```java
public record Engineer(String name, String role, int yearsOfExperience,
                       List<String> domains, List<String> focus, String exploring) {}

var javidan = new Engineer(
    "Javidan Alizada",
    "Senior Software Engineer",
    8,
    List.of("iGaming", "FinTech", "Banking", "GovTech"),
    List.of("distributed systems", "high concurrency", "low latency",
            "event-driven architecture", "observability"),
    "Java 25 · virtual threads · structured concurrency"
);
```

I build backend platforms for real-money, real-time workloads, where **correctness under load**, **predictable latency** and **operability** matter as much as features.

## ⚡ Highlights

- 🚀 Led the re-architecture of a real-time game platform → **300× scalability, 100,000 concurrent clients**
- 🔭 Observability across JVM, gRPC, ZeroMQ & infra → **~85% faster troubleshooting**
- 📨 Event-driven architecture: **Kafka & RabbitMQ pipelines**, Outbox, CDC, Saga, delivery semantics & backpressure
- ⚙️ JVM performance: **concurrency, lock-free algorithms**, GC tuning, reactive programming (WebFlux)
- 🔍 Data & search: **Elasticsearch** indexing/query tuning, PostgreSQL & MongoDB optimization, Redis/Hazelcast caching

## 🏗️ How I Design Real-Time Platforms

```mermaid
flowchart LR
    C["👥 Clients<br/>100K concurrent"] -->|WebSocket| G["Gateway<br/>Netty · Vert.x"]
    G -->|gRPC| GS["Game Services"]
    G -->|gRPC| WS["Wallet Service"]
    GS <-->|ZeroMQ| WS
    GS -->|events| K[("Kafka")]
    WS -->|Outbox · CDC| K
    K --> AN["Analytics &<br/>Async Workflows"]
    GS --> R[("Redis · Hazelcast")]
    WS --> P[("PostgreSQL")]
    OBS["📊 Prometheus · Grafana · Zipkin · ELK"] -.-> G & GS & WS
```

<sub>Reference architecture: horizontally scalable stateless gateways, low-latency service-to-service messaging, transactional event publishing, and end-to-end observability.</sub>

## 🧰 Tech Stack

**Languages & Core**
<br />![Java](https://img.shields.io/badge/Java_8_%7C_17_%7C_21_%7C_25-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

**Backend & Frameworks**
<br />![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white) ![Spring WebFlux](https://img.shields.io/badge/Spring_WebFlux-6DB33F?style=for-the-badge&logo=spring&logoColor=white) ![gRPC](https://img.shields.io/badge/gRPC-244C5A?style=for-the-badge) ![Netty](https://img.shields.io/badge/Netty-4A5568?style=for-the-badge) ![Vert.x](https://img.shields.io/badge/Vert.x-782A90?style=for-the-badge) ![WebSockets](https://img.shields.io/badge/WebSockets-4A5568?style=for-the-badge)

**Messaging & Streaming**
<br />![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white) ![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white) ![ZeroMQ](https://img.shields.io/badge/ZeroMQ-DF0000?style=for-the-badge)

**Data & Storage**
<br />![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white) ![Hazelcast](https://img.shields.io/badge/Hazelcast-2C5BA8?style=for-the-badge) ![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)

**Cloud, DevOps & Observability**
<br />![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

**Architecture**
<br />![Microservices](https://img.shields.io/badge/Microservices-4A5568?style=for-the-badge) ![Event-Driven](https://img.shields.io/badge/Event--Driven-4A5568?style=for-the-badge) ![DDD](https://img.shields.io/badge/DDD-4A5568?style=for-the-badge) ![Hexagonal](https://img.shields.io/badge/Hexagonal-4A5568?style=for-the-badge) ![CQRS](https://img.shields.io/badge/CQRS-4A5568?style=for-the-badge) ![Saga](https://img.shields.io/badge/Saga-4A5568?style=for-the-badge) ![Outbox](https://img.shields.io/badge/Outbox-4A5568?style=for-the-badge)

## 📌 Featured Work

| Project | What it shows |
|---|---|
| 🔒 [**concurrent-collections-lock-free**](https://github.com/JavidanAlizada/concurrent-collections-lock-free) | Lock-free data structures on `VarHandle`: CAS algorithms & Java Memory Model reasoning |
| 🚦 [**resilience-traffic-control**](https://github.com/JavidanAlizada/resilience-traffic-control) | Rate limiting (GCRA, token bucket), timer wheel, retries with jitter, circuit breakers from first principles |
| 🎰 [**matrix-betting-game**](https://github.com/JavidanAlizada/matrix-betting-game) | Real-time betting game engine: probability-based symbol matrix, win combinations, bonus multipliers |
| 📁 [**reactive-file-storage**](https://github.com/JavidanAlizada/reactive-file-storage) | Non-blocking file storage service: Spring WebFlux, reactive MongoDB & Redis, JWT security, OpenAPI, Docker |

## 🧭 Journey

| Period | Domain | Focus |
|---|---|---|
| **2024 – now** | 🎰 iGaming | Real-time game platforms, 100K-client scale, gRPC/ZeroMQ, observability |
| **2023 – 2024** | 🏦 Banking | Risk & compliance services, Elasticsearch search, reactive APIs |
| **2021 – 2023** | 🏛️ GovTech | National e-government platform, team leadership, performance (+150%) |
| **2018 – 2021** | 💳 FinTech | Financial decision engine, event-driven microservices on Kafka |

<details>
<summary><b>🧠 Engineering principles I work by</b></summary>
<br />

- **Measure before optimizing.** Profiles, traces and load tests over intuition.
- **Design for failure.** Timeouts, retries with jitter, circuit breakers and bulkheads by default.
- **Make it observable.** If it isn't in a metric, a trace or a log, it doesn't exist in production.
- **Own it end to end.** From design doc to deployment to on-call.
- **Clear contracts.** Versioned APIs and explicit delivery semantics between services.
- **Simple beats clever,** unless the latency budget says otherwise.

</details>

## ✍️ Writing

<!-- Add article links here as you publish them -->
- *Coming soon:* Building a lock-free MPSC queue on VarHandle

---

<div align="center">

**Let's talk about distributed systems, concurrency or real-time platforms.**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/javidan-alizada-284781153/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:javidanalizada99@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JavidanAlizada)

</div>
