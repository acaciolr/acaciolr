<img src="assets/header.png" alt="Acácio Lima Rocha — Senior Database Administrator" width="100%">

<p align="center">
  <a href="https://www.linkedin.com/in/acaciolr"><img src="https://img.shields.io/badge/LinkedIn-Ac%C3%A1cio%20Lima%20Rocha-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://dbabrabo.com.br"><img src="https://img.shields.io/badge/dbabrabo.com.br-FF8A4C?style=for-the-badge&logo=googlechrome&logoColor=0A0A0A"></a>
  <img src="https://img.shields.io/badge/Oracle%20ACE-Associate-B57BF5?style=for-the-badge&logo=oracle&logoColor=white">
  <img src="https://img.shields.io/badge/Certifica%C3%A7%C3%B5es-14-2ED8C3?style=for-the-badge">
</p>

---

### Senior Database Administrator · 12+ years in mission-critical production

I keep databases alive where downtime has a price tag. Oracle, MySQL, SQL Server and
PostgreSQL — high availability, disaster recovery, performance tuning and the kind of
troubleshooting that happens at 3 a.m. **Oracle ACE Associate**, 14 Oracle credentials,
and a habit of turning what I learn into open-source tooling. I also co-founded
[DBA BRABO](https://dbabrabo.com.br), a technical mentorship program for DBAs in Brazil.

---

## Sobre

Sou DBA há mais de 12 anos, sempre em ambientes onde parada custa caro. Meu trabalho
mora na parte chata e crítica do banco: alta disponibilidade, contingência, recuperação
de desastre, tuning e o troubleshooting que ninguém quer receber de madrugada.

Passei por **Principal Advanced Support Engineer**, **MySQL Tech Lead** e **Consultor DBA
Sênior**. Sou **Oracle ACE Associate** e **LinkedIn Top Database Administration Voice 2024**.

O que eu aprendo apanhando em produção eu transformo em duas coisas: **ferramenta open
source** e **mentoria**. Estão as duas aqui embaixo.

---

## Credenciais

<!-- Para transformar cada medalha em link de verificacao do Credly, envolva a tag <img>
     assim:  <a href="https://www.credly.com/badges/SEU-ID"><img ...></a>
     Os IDs saem do seu perfil do Credly, em cada badge, no botao "Share > Link". -->

<table>
  <tr>
    <td align="center" width="33%"><img src="assets/badges/ace-associate.png" width="96"><br><b>Oracle ACE Associate</b><br><sub>Reconhecimento</sub></td>
    <td align="center" width="33%"><img src="assets/badges/maa.png" width="96"><br><b>Oracle MAA</b><br><sub>Maximum Availability Architecture</sub></td>
    <td align="center" width="33%"><img src="assets/badges/exadata-x9m-specialist.png" width="96"><br><b>Exadata X9M</b><br><sub>Specialist</sub></td>
  </tr>
</table>

**Professional** — o nível mais alto das provas de certificação Oracle

<table>
  <tr>
    <td align="center" width="20%"><img src="assets/badges/oracle-19c-rac-asm-gi.png" width="76"><br><sub>19c RAC, ASM<br>e Grid Infrastructure</sub></td>
    <td align="center" width="20%"><img src="assets/badges/oracle-19c-data-guard.png" width="76"><br><sub>19c<br>Data Guard</sub></td>
    <td align="center" width="20%"><img src="assets/badges/oracle-23ai-professional.png" width="76"><br><sub>23ai<br>Administration</sub></td>
    <td align="center" width="20%"><img src="assets/badges/oracle-db-2019-professional.png" width="76"><br><sub>Database<br>Administration</sub></td>
    <td align="center" width="20%"><img src="assets/badges/mysql-80-dba-professional.png" width="76"><br><sub>MySQL 8.0<br>Administrator</sub></td>
  </tr>
</table>

**Associate** · **Foundations**

<table>
  <tr>
    <td align="center" width="16%"><img src="assets/badges/oracle-23ai-associate.png" width="66"><br><sub>23ai<br>Administration</sub></td>
    <td align="center" width="16%"><img src="assets/badges/mysql-heatwave-associate.png" width="66"><br><sub>MySQL HeatWave<br>Implementation</sub></td>
    <td align="center" width="16%"><img src="assets/badges/mysql-implementation-associate.png" width="66"><br><sub>MySQL<br>Implementation</sub></td>
    <td align="center" width="16%"><img src="assets/badges/oci-foundations.png" width="66"><br><sub>Oracle Cloud<br>Infrastructure</sub></td>
    <td align="center" width="16%"><img src="assets/badges/oracle-cloud-data-management.png" width="66"><br><sub>Cloud Data<br>Management</sub></td>
    <td align="center" width="16%"><img src="assets/badges/oci-ai-foundations.png" width="66"><br><sub>OCI AI<br>Foundations</sub></td>
  </tr>
</table>

---

## Projetos

Tudo roda no terminal, por SSH, sem agente e sem servidor web para expor.

### Monitoração no terminal

#### [ORA BRABO](https://github.com/acaciolr/ora-brabo) · `em produção`

Monitoramento Oracle direto no terminal, construído em Textual. 12 painéis acessíveis por
teclas de função, cobrindo RAC, Data Guard, ASM e Exadata. Os coletores são assíncronos —
a interface não trava esperando query voltar.

#### [SQL BRABO](https://github.com/acaciolr/sql-brabo) · `em produção`

O ORA BRABO para SQL Server — o Activity Monitor que você acessa por SSH. Sessões, Top SQL,
waits, bloqueios, Always On, log shipping, backups, TempDB e um Advisor com regras
automáticas, tudo lido de DMVs, de SQL Server 2012 a 2025, em Windows ou Linux.

#### [PG BRABO](https://github.com/acaciolr/pg_brabo) · `em produção`

*The pgAdmin you SSH into.* Cockpit PostgreSQL no terminal: monitoramento, performance,
backup/recovery, replicação, HA e segurança.

### Diagnóstico, segurança e operação

#### [ORACLE RECOVERY BRABO](https://github.com/acaciolr/oracle-recovery-database-framework) · `em produção`

Orquestrador de backup, restore e recovery Oracle para Unix, guiado pelo princípio
**descobrir → validar → planejar → mostrar comandos → mostrar riscos** antes de executar
qualquer coisa. Shell POSIX (`ksh`/`sh`), 14 áreas.

#### [MyBraboSat](https://github.com/acaciolr/mybrabosat) · `em produção`

Security assessment de MySQL em um único arquivo `.sql`, somente leitura: 53 verificações
em contas, privilégios, rede e criptografia, configuração, auditoria e dados pessoais (LGPD),
cada falha com o comando de correção e a nota de postura de 0 a 100. Sai em HTML
autocontido, em PDF pelo próprio relatório e em texto para ler no terminal.

#### [BSAR — BRABO Slow Analyze Report](https://github.com/acaciolr/bsar) · `em produção`

Analisador de slow query log do MySQL, MariaDB e Percona no estilo AWR: lê do arquivo ou da
`mysql.slow_log`, normaliza e agrega por fingerprint, compara períodos com snapshots em
SQLite e entrega o relatório no terminal e em HTML interativo, com JSON e CSV. Modo watch
com alertas e EXPLAIN das piores queries. Zero dependências externas.

#### [MySQL Export Users](https://github.com/acaciolr/dbabrabo_mysqlexportusers) · `em produção`

Extensão nativa do **MySQL Shell** que exporta usuários, roles e privilégios em SQL
idempotente, gera `REVOKE`s para rollback e auditoria e converte sintaxe MariaDB → MySQL.
Pronto para Git e para replay entre ambientes.

### Laboratórios Super DBA

Uma plataforma de laboratório por tecnologia, construída para a mentoria
[DBA BRABO](https://github.com/DBA-BRABO): instala com um comando, sobe os nós e abre um
menu em que cada opção executa operação real sobre o banco — e termina com `PASS` ou `FAIL`.

| Laboratório | Estado | O que cobre |
| --- | --- | --- |
| **SQL Server Super DBA** | `testado em ambiente real` | SQL Server 2022/2025 em Linux: Always On com Pacemaker + listener, log shipping, replicação, PITR, TDE/TLS, IA no 2025 |
| **PostgreSQL Super DBA** | `em homologação` | replicação, HA, backup/PITR, upgrade, pooling, pgvector, chaos — 112 tópicos executáveis |
| **MySQL Super DBA** | `em homologação` | 19 topologias: InnoDB Cluster, Group Replication, NDB, Percona XtraDB Cluster, caos e recuperação |
| **Oracle Super DBA** | `em desenvolvimento` | VMs Oracle Linux reais: RAC com ASM, Data Guard, Exadata e ZDLRA |
| **MongoDB Super DBA** | `em desenvolvimento` | replica set e sharding |

Os laboratórios são privados: o acesso é liberado para os mentorados da DBA BRABO.

---

## Stack

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![GoldenGate](https://img.shields.io/badge/GoldenGate-F80000?style=flat-square&logo=oracle&logoColor=white)

![Exadata](https://img.shields.io/badge/Exadata-C74634?style=flat-square&logo=oracle&logoColor=white)
![OCI](https://img.shields.io/badge/OCI-F80000?style=flat-square&logo=oracle&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

## DBA BRABO

Mentoria técnica para DBAs que fundei com Luis Macedo e Weverton Amorim. Não é curso gravado: é acompanhamento em
cima de ambiente real, com trilha por tecnologia — Oracle, MySQL, SQL Server, PostgreSQL,
MongoDB, GoldenGate, Exadata, ODA, ZDLRA e as três nuvens.

**[dbabrabo.com.br](https://dbabrabo.com.br)** · [LinkedIn](https://www.linkedin.com/company/dbabrabo) · [@dbabrabo](https://instagram.com/dbabrabo)

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=acaciolr&show_icons=true&hide_border=true&bg_color=0D1117&title_color=FF8A4C&icon_color=2ED8C3&text_color=C9D1D9" height="150">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=acaciolr&layout=compact&hide_border=true&bg_color=0D1117&title_color=FF8A4C&text_color=C9D1D9" height="150">
</p>

<p align="center"><sub>Se o banco caiu e ninguém sabe por quê, é sobre isso que eu converso melhor.</sub></p>
