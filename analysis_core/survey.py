def probability_rows(rows):
    """筛选具备概率抽样权重的入户回答。"""
    return [dict(r) for r in rows if r['source']=='household' and r['weight'] is not None]

def weighted_unmet(rows):
    """计算原始入户权重下的未满足比例。"""
    rows=probability_rows(rows)
    denominator=sum(r['weight'] for r in rows if r['unmet'] is not None)
    return None if not denominator else sum(r['weight']*r['unmet'] for r in rows if r['unmet'] is not None)/denominator

def replicate_columns(rows):
    """读取入户资料的重复权重列，保持重复序号一致。"""
    rows=probability_rows(rows)
    sizes={len(r['replicate_weights']) for r in rows}
    if len(sizes)>1:
        raise ValueError('inconsistent replicate count')
    n=next(iter(sizes),0)
    return [[r['replicate_weights'][i] for r in rows] for i in range(n)]

def source_counts(rows):
    """核对回答来源数量，不以人数解释回答条数。"""
    result={}
    for row in rows:
        result[row['source']]=result.get(row['source'],0)+1
    return result
