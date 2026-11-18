# 资料交换约定

资料为 UTF-8 JSON，根对象包含 name、tables 和 options。tables 的每张表都必须出现，允许空表；记录中的约定字段必须存在，显式 null 保留来源未知的含义，不能与字段缺失混淆。额外字段及 options 可承载研究方案。金额和时间的具体口径如下。

| 表 | 字段 |
| --- | --- |
| responses | response, source, person, candidate_group, district, age, urban, sex, unmet, weight, stratum, psu, replicate_weights |
| margins | margin, cells, lower, upper |
| links | left, right, relation |

unmet 是 0/1/null；重复权重方案使用 BRR，重复次数及 Fay 系数由输入 design 给定，缺失 design 时不得计算设计方差。links.relation 为 same/different/candidate；candidate 同组列出可兼容对应，不等于确认同人。margins.cells 指定一个人口单元的筛选属性，lower/upper 为该单元人数约束。

options.design 包含 method=BRR、replicates 和 fay（0≤fay<1）；重复权重已由抽样方生成，序号跨全部入户行对齐。links 可附加 world 指明同一兼容对应方案；有 candidate 但缺少兼容方案时，不应把候选当确认关联。控制总量上下界均为人数，比例不是合法替代。

analysis_core/survey.py 中的公开函数用于原始核对。probability_rows 保留当前参数及返回语义。原始资料查询不代表已经完成统计识别或政策判断。examples/study.json 是可读的合成资料，数值不表示真实地区或人群。

Archive 用 name 和完整内容摘要区分原始资料修订。相同内容重复存入不会增加修订，不同内容不会覆盖旧资料；read 以精确摘要读取。Study.tables 和 Study.options 每次返回独立副本。group_rows 用属性是否存在与属性值共同分组；numeric_summary 分别报告条数、有效数值及空值。已有资料结构、原始查询及归档读取继续对外可用。
