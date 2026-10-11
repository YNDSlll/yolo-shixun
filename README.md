# 交通标志检测与人脸表情识别

<div align="left">
  <img alt="项目标签" src="https://img.shields.io/badge/项目类型-计算机视觉-0A66C2" />
  <img alt="任务类型" src="https://img.shields.io/badge/任务-交通标志+人脸表情-FF6B6B" />
  <img alt="算法框架" src="https://img.shields.io/badge/框架-YOLO-00C2A8" />
  <img alt="界面" src="https://img.shields.io/badge/演示-Streamlit-7C3AED" />
  <a href="https://yolo-shixun.streamlit.app/"><img alt="在线演示" src="https://img.shields.io/badge/在线演示-Streamlit%20Cloud-FF4B4B" /></a>
</div>

这是一个面向智能交通与情绪交互场景的计算机视觉项目，基于 Ultralytics YOLO 实现交通标志识别与人脸表情识别，并通过 Streamlit 构建可视化演示界面。

项目覆盖从数据准备、模型训练、结果评估到应用展示的完整流程，能够在本地环境中快速验证模型效果，并为后续功能扩展提供可复用的开发基础。

- 交通标志检测：面向道路场景中的交通信息识别与安全辅助
- 人脸表情识别：用于情绪状态分析与人机交互场景的视觉理解

## 在线体验

项目已部署到 Streamlit Community Cloud，不需要配置任何本地环境，打开浏览器就能直接试用：

| 项目 | 内容 |
| --- | --- |
| 访问地址 | https://yolo-shixun.streamlit.app/ |
| 登录账号 | `lhy` |
| 登录密码 | `111` |

使用步骤：打开上面的地址 → 输入账号密码登录 → 左侧菜单选择「交通标志检测」或「人脸表情检测」→ 上传一张图片 → 点击「开始检测」。

> 说明：应用长时间无人访问会自动休眠，再次打开需要约 1 分钟冷启动，页面提示「Please wait」时稍等片刻即可。
> 该账号是演示用固定账号，不涉及任何真实用户数据。

## 项目亮点

- 基于 YOLO 的端到端检测流程
- 使用 Streamlit 构建轻量 Web 界面，并已部署到公网
- 支持两类自定义检测任务
- 随仓库提供两个自训练模型权重，克隆后即可直接推理
- 提供演示截图与推理示例脚本

## 核心功能

### 1. 交通标志检测

系统能够识别常见交通标志类别，包括禁止标志、危险标志、强制标志以及其他相关类别，适用于智能交通和辅助驾驶场景。

### 2. 人脸表情识别

项目支持八类表情识别，包括愤怒、轻蔑、厌恶、恐惧、开心、中性、悲伤和惊讶，适用于情绪分析和人脸检测场景。

### 3. Web 应用界面

通过上传图片即可完成识别，并展示原图与检测结果图，界面由 Streamlit 提供，适合本地演示和功能展示。

### 4. 模型推理与分析

仓库中包含：

- 单张图像推理示例
- 摄像头实时推理示例
- 检测结果解析
- 训练结果概览截图（混淆矩阵、训练曲线）

## 项目结构

```text
.
├── app.py                              # Streamlit 主程序（登录 + 两类检测页面）
├── 01-预训练模型推理一张图片.py
├── 02-预训练模型推理摄像头.py
├── 03-推理结果解析.py
├── environment-shixun.yml              # 本地 conda / mamba 环境清单
├── requirements.txt                    # 部署依赖清单（Streamlit Cloud 读取此文件）
├── packages.txt                        # 系统级依赖（opencv 所需的 libGL 等）
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── datasets/                           # 训练数据集（体积较大，未随仓库发布）
│   ├── traffic_signal/
│   └── FacialExpression/
├── runs/detect/trains/                 # 训练产物，仅随仓库发布两个 best.pt
│   ├── train-TrafficSignal/weights/best.pt
│   └── train-FacialExpression/weights/best.pt
├── images/                             # 运行时自动创建，不随仓库发布
│   ├── upload/                         # 上传的待检测图片
│   └── result/                         # 检测结果图片
├── screenshots/
│   ├── traffic_signal_demo.jpg
│   ├── facial_expression_demo.jpg
│   ├── traffic_results.png
│   └── facial_results.png
└── ultralytics/                        # YOLO 框架源码
```

## 关于文件

本项目的关键文件职责如下：

- `app.py`：主界面程序，整合登录页、首页和两类检测功能，负责加载模型并调用 Streamlit 展示检测结果。
- `01-预训练模型推理一张图片.py`：演示单张图片推理流程，适用于快速验证模型效果。
- `02-预训练模型推理摄像头.py`：基于本地摄像头实时检测，可用于现场演示和实验验证。
- `03-推理结果解析.py`：读取并解析检测输出，提取类别、置信度和边界框信息，便于结果分析。
- `environment-shixun.yml`：本地 conda / mamba 环境清单，由 `mamba env export -n shixun --no-builds` 导出，用于复现本地开发环境。文件名刻意不叫 `environment.yml`，避免被 Streamlit Cloud 识别成 conda 依赖文件（见下节说明）。
- `requirements.txt`：Python 依赖清单，Streamlit Cloud 会自动读取并安装。
- `packages.txt`：系统级依赖清单，主要是 `opencv` 在 Linux 上需要的 `libGL`。
- `pyproject.toml`：Ultralytics 库自带的构建元数据（描述 `ultralytics` 包本身），**不是**本项目的部署清单。它在 Streamlit Cloud 的依赖文件优先级里排在最后，且仓库中已有 `requirements.txt`，因此云端不会读取它。
- `datasets/traffic_signal/`：交通标志数据集目录，包含训练/验证数据与配置文件。
- `datasets/FacialExpression/`：表情数据集目录，包含训练/验证数据与配置文件。
- `runs/`：训练产物目录。为了避免仓库过大，仅随仓库发布两个 `best.pt` 权重，验证预测图、混淆矩阵、训练曲线等中间产物不入库。
- `images/`：运行时创建的图片目录，保存用户上传的原图与检测结果图，程序会自动建立，不随仓库发布。
- `screenshots/`：项目展示图，主要用于 GitHub 介绍页和效果展示。
- `ultralytics/`：项目依赖的 Ultralytics YOLO 实现代码，提供模型推理和训练能力。

## 效果展示

### 交通标志检测

![交通标志检测效果](screenshots/traffic_signal_demo.jpg)

### 人脸表情识别

![人脸表情识别效果](screenshots/facial_expression_demo.jpg)

### 训练结果概览

![交通标志训练结果](screenshots/traffic_results.png)

![人脸表情训练结果](screenshots/facial_results.png)

## 数据与模型

仓库中随项目发布的权重只有两个，都是本项目自训练得到的：

| 权重文件 | 类别数 | 用途 |
| --- | --- | --- |
| `runs/detect/trains/train-TrafficSignal/weights/best.pt` | 4 类交通标志 | 交通标志检测页面加载的模型 |
| `runs/detect/trains/train-FacialExpression/weights/best.pt` | 8 类人脸表情 | 人脸表情检测页面加载的模型 |

两个模型的类别如下：

- 交通标志（4 类）：`prohibitory`（禁止）、`danger`（危险）、`mandatory`（强制）、`other`（其他）
- 人脸表情（8 类）：`Anger`、`Contempt`、`Disgust`、`Fear`、`Happy`、`Neutral`、`Sad`、`Surprise`

此外，仓库中的推理示例脚本使用官方 COCO 预训练权重 `yolo26n.pt`（80 类通用目标）来跑通推理流程。该权重体积较大且可以自动获取，因此没有随仓库发布，首次运行脚本时由 Ultralytics 自动下载到项目根目录。

数据集不随仓库发布，训练过程中的验证预测图、混淆矩阵与训练曲线同样未入库，仓库中只保留两个可直接用于推理的 `best.pt`。

## 发布说明

本仓库作为一个基于 YOLO 的计算机视觉示例项目，旨在提供一个简洁、可运行、便于演示和扩展的参考实现，涵盖本地推理、模型评估和应用层集成等关键流程。

重点特性包括：

- 基于 Ultralytics YOLO 框架
- 随仓库提供两个自训练检测模型，可直接推理
- 提供 Streamlit 可视化界面，并已部署到 Streamlit Cloud
- 适用于智能交通、人脸识别与扩展型视觉应用

## 环境依赖

### 本地开发环境（conda / mamba）

本地使用 miniforge 管理环境，完整清单见仓库根目录的 `environment-shixun.yml`（Python 3.11.15 + conda-forge）：

```bash
# 已有环境，直接激活
mamba activate shixun

# 或者在新机器上按清单复现
mamba env create -f environment-shixun.yml
mamba activate shixun
```

当前 `shixun` 环境已验证可运行，核心依赖如下：

```text
python==3.11.15
streamlit==1.56.0
ultralytics==8.4.39
pytorch==2.10.0
torchvision==0.26.0
opencv==4.13.0
numpy==2.4.3
pandas==3.0.2
matplotlib==3.10.8
pillow==12.2.0
pyyaml==6.0.3
requests==2.33.1
scipy==1.17.1
psutil==7.2.2
polars==1.40.0
```

如需重新导出完整清单，可在项目根目录执行：

```bash
mamba env export -n shixun --no-builds > environment-shixun.yml
```

> ⚠️ 导出时请保持 `environment-shixun.yml` 这个文件名，**不要**改成 `environment.yml`：Streamlit Cloud 会按 `uv.lock > Pipfile > environment.yml > requirements.txt > pyproject.toml` 的优先级挑选依赖文件，且只用找到的第一个。一旦出现 `environment.yml`，云端就会改用 conda 去解这份 macOS 专用清单，导致构建失败或长时间卡在 `Solving environment`。

### 云端部署环境（pip）

云端不需要 conda，以 `requirements.txt` 为准：

```bash
pip install -r requirements.txt
```

需要注意，Streamlit Cloud 的 Python 版本**不能通过仓库里的文件指定**（`runtime.txt` 在该平台不生效），必须在部署时的 `Advanced settings` 里手动选择。本项目已选 **3.11**，详见下一节。

另外，云端 pin 的版本可能与本地 conda 环境略有差别，这是正常的：conda-forge 与 PyPI 的依赖元数据并不一致。例如本地 conda 装的 `torchvision 0.26.0` 可以和 `pytorch 2.10.0` 共存，但 CPU 源（PyPI 体系）上的 `torchvision 0.26.0` 要求 `torch==2.11.0`，因此 `requirements.txt` 里把两者成对固定为 `torch==2.11.0` + `torchvision==0.26.0`。

> 提示：`requirements.txt` 中的 torch / torchvision 只写基础版本号、不写 `+cpu` 后缀。Linux 上 pip 会自动选中 `2.11.0+cpu`（本地版本号高于 `2.11.0`），而 macOS 上正常从 PyPI 安装；若写死成 `+cpu`，本地 pip 安装会因缺少 macOS 轮子而失败。

### 运行 Web 应用

```bash
streamlit run app.py
```

### 运行单张图片推理

```bash
python 01-预训练模型推理一张图片.py
```

### 运行摄像头推理

```bash
python 02-预训练模型推理摄像头.py
```

### 解析检测结果

```bash
python 03-推理结果解析.py
```

## 云端部署（Streamlit Community Cloud）

本项目已完成 Streamlit Community Cloud 免费部署，公网地址见「在线体验」一节。

### 当前部署状态

| 项目 | 内容 |
| --- | --- |
| 部署状态 | 已上线 |
| 应用地址 | https://yolo-shixun.streamlit.app/ |
| 仓库 / 分支 | `YNDSlll/yolo-shixun` / `main` |
| 入口文件 | `app.py` |
| 云端 Python | 3.11（在 `Advanced settings` 中指定） |
| 依赖来源 | `requirements.txt`（pip）+ `packages.txt`（apt 系统库） |

### 部署所需文件（已随仓库提供）

- `requirements.txt`：Python 依赖清单，云端会自动读取并安装
- `packages.txt`：系统级依赖（`libgl1`、`libglib2.0-0`），避免 `opencv` 在 Linux 上报 `libGL.so.1` 缺失
- 模型权重：两个自训练 `best.pt` 已随仓库发布（交通标志 4 类、人脸表情 8 类）
- `app.py`：按脚本所在目录定位资源，并对模型启用缓存，避免每次点击都重新加载权重

> ⚠️ `packages.txt` 的内容会被整份交给 `apt-get install`，**只能一行一个包名，不能写任何注释**。写了 `#` 注释会被当成包名，报出 `E: Unable to locate package #` 这类错误，导致依赖安装整体失败（`requirements.txt` 不受影响，pip 是支持注释的）。
>
> ⚠️ 仓库根目录**不要出现名为 `environment.yml` 的文件**。Streamlit Cloud 按 `uv.lock > Pipfile > environment.yml > requirements.txt > pyproject.toml` 的优先级挑选依赖文件，且只用找到的第一个；`environment.yml` 排在 `requirements.txt` 前面，会被云端当成 conda 依赖交给 conda 解析，构建会失败或长时间卡在 `Solving environment`。本项目的本地环境清单因此命名为 `environment-shixun.yml`。

### 部署步骤

1. 打开 [share.streamlit.io](https://share.streamlit.io/)，用 GitHub 账号登录并授权。
2. 点击右上角 `Create app`，选择 `Deploy a public app from GitHub`。
3. 按下表填写配置：

   | 配置项 | 填写内容 |
   | --- | --- |
   | Repository | `YNDSlll/yolo-shixun` |
   | Branch | `main` |
   | Main file path | `app.py` |
   | App URL | 自定义子域名，例如 `yolo-shixun` |

   > 仓库下拉框里的候选列表**不一定完整**，如果没有出现 `yolo-shixun`，直接在输入框里手动敲完整仓库名 `YNDSlll/yolo-shixun` 即可，或者用 `Paste GitHub URL` 粘贴仓库地址。

4. 展开 `Advanced settings`，把 `Python version` 选成 **3.11**（与本地 `shixun` 环境一致）。
   云端默认版本更高（可能是 3.14），而 `torch==2.11.0` 等依赖在过新的 Python 上往往还没有可用的安装包，构建会直接失败。`Secrets` 一栏留空即可，本项目未使用 Secrets。
5. 点击 `Deploy`，等待依赖安装与构建完成，首次构建通常需要 5～10 分钟。
6. 构建成功后页面会给出公网地址，形如 `https://<应用名>.streamlit.app`。

本项目已按上述步骤完成部署，最终地址就是「在线体验」一节里的 `https://yolo-shixun.streamlit.app/`，无需再回填。

部署完成后如果还要调整 Python 版本，可以在应用页面右侧的 `⋮` → `Settings` → `Advanced settings` 里改，改完重启应用生效。

### 常见问题

| 现象 | 原因与处理 |
| --- | --- |
| 报 `E: Unable to locate package #`（后面还跟着一堆中英文单词） | `packages.txt` 里写了注释，apt 把注释文字也当成包名去装了。该文件只能一行一个包名，删掉注释后重新推送 |
| 报 `ResolutionImpossible` / `these package versions have conflicting dependencies` | torch 与 torchvision 版本没配对上。torchvision 会锁定确切的 torch 版本，两者必须成对修改 |
| 长期卡在 `Solving environment`，或依赖解析失败 | 根目录出现了 `environment.yml`，云端改用 conda 解析。把它改名（本项目为 `environment-shixun.yml`）后重新推送 |
| 下拉列表里找不到本仓库 | 候选列表不完整，手动输入 `YNDSlll/yolo-shixun`，或用 `Paste GitHub URL` |
| 用 `curl` 或提交到第三方平台时被 303 跳转到 `share.streamlit.io/-/auth/app` | 这是 Cloud 对**没有会话 Cookie 的请求**做的统一认证跳转，**公开应用同样如此**，不代表应用被设成了私有。用浏览器正常打开即可。已实测 Streamlit 官方的 `llm-examples`、`datasets` 等公开应用返回结果完全一致 |
| 报 `No matching distribution found for torch==...` | Python 版本太新，在 `Advanced settings` 里改成 3.11 后重新部署 |
| 报 `ModuleNotFoundError` | 确认 `requirements.txt` 已推送到 `main` 分支 |
| 报 `libGL.so.1: cannot open shared object file` | 确认 `packages.txt` 已推送，然后在控制台点 `Reboot app` |
| 点击检测报「模型文件缺失」 | 权重没进仓库，检查 `runs/detect/trains/*/weights/best.pt` 是否已推送 |
| 首次打开很慢 | 免费版应用长时间无人访问会休眠，冷启动约需 1 分钟 |
| 安装体积过大或超时 | 确认 `requirements.txt` 里的 `--extra-index-url https://download.pytorch.org/whl/cpu` 还在，避免安装 CUDA 版 torch |

## 说明

- 应用已上线，线上地址为 <https://yolo-shixun.streamlit.app/>；本地用 `streamlit run app.py` 运行，两端功能与界面一致
- 线上只加载两个自训练的 `best.pt`，**不会**触发 `yolo26n.pt` 的自动下载——该权重仅被 `01` / `02` 号示例脚本使用
- `app.py` 中的登录系统为简单演示用认证，账号密码固定写在代码里，不用于正式生产环境
- 仓库为公开仓库，演示账号也一并公开，请勿在其中存放任何真实数据
- 项目可进一步扩展到交通监控、安全检测、人机交互等实际场景

## 许可证

本项目遵循 Ultralytics 代码库所采用的 AGPL-3.0 许可证，完整条款请见 [LICENSE](LICENSE)。

## 总结

该仓库展示了一个结构清晰、可运行、可演示的 YOLO 计算机视觉应用，包含自训练模型权重、推理脚本、演示素材与 Web 界面，既可克隆到本地运行，也可直接通过云端地址在线体验，适合用于项目展示、技术评审以及后续功能扩展。
