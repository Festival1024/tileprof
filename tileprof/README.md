# 介绍
这是一个以分块为中心的GPU内核性能剖析器protile，旨在高效剖析内核配置性能并计算出最优配置，编译生成内核代码。
它面向当前day0开发对高效率内核编程的需求，适应当前以分块为中心的内核编程特点，通过对数据块在GPU上传输与计算过程进行建模，定量分析内核执行中所有数据块的处理时延，无须实际执行内核即可推理得到最优的内核配置。相比以往基于程序追踪的、基于roofline模型的、基于学习模型的剖析器，本剖析器直接计算并得出最优的内核配置，降低了剖析时延，具有可移植性强的优点，有效降低内核开发的时间成本，为内核性能提供定量分析的理论支撑。
文件布局如下，按照python项目规范：
protile/                # 项目根目录
├── setup.py               # 安装配置
├── requirements.txt       # 依赖
├── README.md
├── src/                   # 源代码
│   └── protile/        # 主包
│       ├── __init__.py    # 包初始化，导出主要API
│       ├── utils.py       # KernelType, BottleneckType
│       ├── architecture.py # ArchitectureFeatures
│       ├── kernel_features.py # KernelFeatures
│       ├── performance_model.py # PerformanceModel
│       ├── profiler.py    # KernelProfiler
│       ├── autoprofile.py # 自动剖析
│       ├── architecture_lib.py # 芯片库
│       ├── kernel_lib.py  # 内核实现和设计空间
│       └── optimizer.py   # 优化建议
├── tests/                 # 测试
│   ├── __init__.py
│   └── test_profiler.py
├── examples/              # 示例
│   └── gemm_compare_rank.py
└── scripts/               # 脚本
    └── run_benchmark.py


# 如何运行
安装开发模式
pip install -e .

或者设置PYTHONPATH
export PYTHONPATH=/path/to/protile/src:$PYTHONPATH

运行示例
python examples/gemm_compare_rank.py