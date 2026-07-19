# 🔥 开源中文医疗大模型

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork)

本仓库收集了开源中文医疗大模型（中医/西医）相关的资源，包括新闻、论文、模型、数据集等，欢迎大家贡献更多资源。

**相关链接**：[中医门户](https://tyang816.github.io/tcm/) · [作者中文主页](https://tyang816.github.io/zh/) · [Author site (EN)](https://tyang816.github.io/)

> 门户支持标签筛选与搜索，数据与本 README 同源（`data/catalog.yml`）。

## 📰 新闻
- [2026.06] 中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.04] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型 [[链接](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2025.12] 吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型 [[链接](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.12] 固生堂发布”中医大脑”产品及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身，覆盖八大中医核心专科 [[链接](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] **智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用 [[链接](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.11] 国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型 [[链接](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.09] 传神语联**任度·素问**通过中国信通院可信AI中医药大模型4+级评估 [[链接](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] **智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识 [[链接](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.08] **固生堂**正式发布十大”国医AI分身”，基于国医大师及名中医临床经验构建，辨证准确性达86%以上 [[链接](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.06] **中医横琴**垂类大模型正式发布 [[链接](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] 中国中医科学院发布中医药大模型评测标准 [[链接](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] 传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐 [[链接](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03] 中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院 [[链接](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2024.09] 中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍训练 [[链接](https://36kr.com/newsflashes/2946967562099592)]
- [2024.03] 华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室、华润江中现代中药全国重点实验室联合开发了**数智岐黄**中医药大模型。

## 📚 资源

### 2026
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架 [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理 [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- **MMIR-TCM** 记忆增强的多模态舌诊与临床决策框架，提出 MedTCM 数据集与 TDEU 评测指标 [[论文](https://arxiv.org/abs/2607.01814)]
- **灵兰秘典 (LingLan)** 大规模多任务中医评测基准，覆盖 5 大域、13 子任务、25624 实例 [北京交通大学等] [[论文](https://arxiv.org/abs/2602.01779)] [[代码](https://github.com/TCMAI-BJTU/LingLan)] [[网站](http://tcmnlp.com)]
- **TCM-Agent** 面向网络药理学与中药发现的 LLM 多智能体系统 [[论文](https://doi.org/10.1016/j.jpha.2026.101581)] [[代码](https://github.com/AITCM/TCM-Agent)]
- **TCM-DiffRAG** 通用知识图谱 + 个性化知识图谱 + CoT 的辨证推理 RAG 框架 [[论文](https://arxiv.org/abs/2602.22828)] [[代码](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- **CORE-Acu** 针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环 [[论文](https://arxiv.org/abs/2603.08321)]

### 2025
- [*Cell Discovery*] **神农Alpha** 中药大模型 [西湖大学] [[网站](https://shennongalpha.westlake.edu.cn/)] [[论文](https://www.nature.com/articles/s41421-025-00776-2)] [[代码](https://github.com/shennong-program/shennongname)]
- [*Pharmacological Research*] **TCMChat** 中药知识聊天机器人 [浙江大学] [[论文](https://doi.org/10.1016/j.phrs.2024.107012)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1043661824004754)] [[代码](https://github.com/ZJUFanLab/TCMChat)] [[模型](https://huggingface.co/ZJUFanLab/TCMChat-600k)] [[数据集](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- [*Tsinghua Science and Technology*] **仲景 (ZhongJing)** 中医大模型 [福耀科技大学，健康长三角研究院，复旦大学，同济大学] [[论文](https://doi.org/10.26599/TST.2025.9010046)] [[代码](https://github.com/pariskang/CMLM-ZhongJing)] [[模型](https://huggingface.co/CMLM/ZhongjingGPT1_13B)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*NeurIPS 2025*] **TCM-Ladder** 首个中医多模态问答评测基准，涵盖52000+题目 [[论文](https://arxiv.org/abs/2505.24063)] [[代码](https://github.com/orangeshushu/TCM-Ladder)] [[榜单](https://tcmladder.com)]
- **经方 (Jingfang)** 基于LLM的中医多智能体诊疗系统，辨证精度提升124% [[论文](https://arxiv.org/abs/2502.04345)]
- **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- **ShizhenGPT** 中医多模态大模型，支持望闻问切 [香港中文大学(深圳)等] [[论文](https://arxiv.org/abs/2508.14706)] [[代码](https://github.com/FreedomIntelligence/ShizhenGPT)] [[模型](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[预训练数据](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)] [[指令数据](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **DoPI** 类医生主动问诊中医大模型，引导模型+专家模型协同架构，问诊准确率84.68% [[论文](https://arxiv.org/abs/2507.04877)]
- **MTCMB** 中医多任务评测基准，12子集约7100样本，覆盖知识/推理/方剂/安全 [[论文](https://arxiv.org/abs/2506.01252)] [[代码](https://github.com/Wayyuanyuan/MTCMB)]
- **TCM-3CEval** 中医大模型三轴评测（核心知识、经典理解、临床决策） [[论文](https://arxiv.org/abs/2503.07041)]
- **OpenTCM** 基于 GraphRAG 的中医知识检索与诊断系统，含妇科古籍知识图谱 [[论文](https://arxiv.org/abs/2504.20118)] [[代码](https://github.com/OpenTCM01/OpenTCM)]
- **ChatTCM** 从预训练数据到模型权重完全开源的中医大模型 [[模型](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)] [[预训练数据](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)] [[SFT数据](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCM-5CEval** 在 TCM-3CEval 基础上扩展本草与非药物疗法的五维深度评测 [[论文](https://arxiv.org/abs/2511.13169)]
- **TCM-BEST4SDT** 面向辨证论治的病例评测基准（知识/伦理/安全/SDT） [[论文](https://arxiv.org/abs/2512.02816)] [[代码](https://github.com/DYJG-research/TCM-BEST4SDT)]
- **仁术AI (RenShu-AI)** FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM [[代码](https://github.com/yanlinPeng-code/RenShu-AI)]

### 2024
- [*Computers in Biology and Medicine*] **MedChatZH** 中医问诊大模型 [华东理工大学] [[论文](https://doi.org/10.1016/j.compbiomed.2024.108163)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010482524003743)] [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)] [[模型](https://huggingface.co/tyang816/medchatzh)] [[代码](https://github.com/tyang816/MedChatZH)]
- [*Digital Chinese Medicine*] **TCMLLM / 灵丹 (Lingdan)** 中医药大模型与处方推荐 [北京交通大学] [[论文](https://doi.org/10.1016/j.dcmed.2025.01.007)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589377725000072)] [[代码](https://github.com/2020MEAI/TCMLLM)] [[灵丹代码](https://github.com/TCMAI-BJTU/LingdanLLM)] [[模型](https://huggingface.co/TCMLLM/Lingdan-13B-Base)]
- **明医 (MING)** 中文医疗问诊大模型 [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*ACM Trans. Knowl. Discov. Data*] **本草[原名：华驼(HuaTuo)]** 基于中文医学知识的大语言模型指令微调 [哈尔滨工业大学] [[论文](https://arxiv.org/pdf/2309.04175.pdf)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- **扁仓 (BianCang)** 系列中医大模型，2025.12 开源 14B 版本 [齐鲁工业大学] [[论文](https://arxiv.org/abs/2411.11027)] [[代码](https://github.com/QLU-NLP/BianCang)] [[模型](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)]
- **大数中医 (BigDataTCM)** 中医垂直领域大模型 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- **MCM** 多模态中医药问诊大模型 [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)]
- **Chinese-LLaVA-Med** 中文医学多模态大模型 [[代码](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]

### 2023
- [*EMNLP findings*] **华佗GPT** 中文医学语料训练的大型语言模型 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://aclanthology.org/2023.findings-emnlp.725/)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT)]
- **扁鹊 (BianQue)** 中文领域生活空间主动健康大模型 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)]
- **黄帝 (HuangDi)** 中医古籍知识问答大模型 [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]
- **启真医学大模型 (QiZhenGPT)** 中文医疗场景、药品知识问答、优化疾病、手术、检验等 [浙江大学] [[代码](https://github.com/CMKRG/QiZhenGPT)]
- **神农大模型 (ShenNong-TCM-LLM)** 中医药大规模语言模型 [[代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM)] [[数据集](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)] [[模型](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- **孙思邈 (Sunsimiao)** 中文医疗大模型 [华东理工大学] [[代码](https://github.com/X-D-Lab/Sunsimiao)]
- **ChatMed** 系列中文医疗大规模语言模型 [[代码](https://github.com/michael-wzhu/ChatMed)]
- **XrayGLM** 会看胸部X光片的中文多模态医学大模型 [澳门理工大学] [[代码](https://github.com/WangRongsheng/XrayGLM)]

## 📚 数据集

### 公开资料整理
- awesome_Chinese_medical_NLP [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]

### 原始书籍 / 预训练语料
- 700 项中医药古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- 中医经典全文语料（内经/伤寒/金匮/温病等 115 部） [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- ShizhenGPT 中医预训练语料（约 6B tokens，含图文交错数据） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- 高质量中医预训练数据集（医案/典籍/百科等） [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]

### 评测基准
- LingLan（灵兰秘典）大规模多任务中医评测基准 (2026) [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779)]
- TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025) [[数据集](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)]
- MTCMB 中医多任务评测基准（知识/推理/安全） [[数据集](https://github.com/Wayyuanyuan/MTCMB)] [[论文](https://arxiv.org/abs/2506.01252)]
- TCM-3CEval 核心知识·经典理解·临床决策三轴评测 [[论文](https://arxiv.org/abs/2503.07041)]
- TCM-5CEval 五维中医深度评测 [[论文](https://arxiv.org/abs/2511.13169)]
- TCM-BEST4SDT 辨证论治病例评测基准 [[数据集](https://github.com/DYJG-research/TCM-BEST4SDT)] [[论文](https://arxiv.org/abs/2512.02816)]
- TCM-Eval 动态可扩展中医评测基准 [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- TCMBench 中医药大模型全面评测基准 [[数据集](https://github.com/ywjawmw/TCMBench)] [[论文](https://arxiv.org/abs/2406.01126)]
- ZhongJing-OMNI 中医多模态评测（含舌诊） [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- TCMEval-SDT 辨证思维评测（专家标注病案） [[论文](https://www.nature.com/articles/s41597-025-04772-9)] [[代码](https://github.com/zhuyan166/TCMEval)]
- HWTCMBench 中医能力评测集 [[数据集](https://huggingface.co/datasets/Monor/hwtcm)]

### 考试数据集
- 医疗大模型中文考试评估 [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- TCM-Text-Exams 近年中医执业/考研真题文本基准 [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]

### 指令/对话数据集
- 中医药指令数据集 ShenNong_TCM_Dataset [[数据集](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- 中文医疗在线问诊数据集 ChatMed_Consult_Dataset（50w+在线问诊+ChatGPT回复） [[数据集](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- MedChatZH 中医问诊数据集 [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)]
- CMtMedQA 仲景真实多轮医患对话（约 7 万条） [[数据集](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- TCMChat-dataset-600k 中药知识问答与推荐指令数据 [[数据集](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- ShizhenGPT 多模态指令微调数据（文本/视觉/语音，约 245K） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- 高质量中医 SFT 数据集 [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]

### 知识图谱
- ChatMed 知识图谱 [[数据集](https://github.com/ywjawmw/TCM_KG)]
- OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系） [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]
- TCM-MKG 中医药多维知识图谱 [[数据](https://zenodo.org/records/15395588)]

### Hugging Face 开源模型（精选）
- ShizhenGPT 系列 [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- 扁仓 (BianCang) 系列 [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]
- TCMChat [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- 仲景 [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- 灵丹 [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- MedChatZH [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- 神农 [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- ChatTCM [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
