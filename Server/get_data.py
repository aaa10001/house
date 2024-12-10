import pandas as pd

# 读取 Excel 文件
file_path = "C:\\Users\\26852\\Desktop\\6565bb8bbd4e692563087b500be35125_addc1d6cc5c0860f19fb4dc869300bc5_8.xlsx"
df = pd.read_excel(file_path)

def get_district_sum():
    # 统计每个区的数据数量，包括空值
    district_counts = df['房屋所属区'].value_counts(dropna=False)

    # 将空值替换为一个明确的标签，例如 '无'
    district_counts.index = district_counts.index.fillna('空值')

    # 创建一个新的 DataFrame，包含两列：'区名' 和 '销售数量'
    result_df = pd.DataFrame({
        '区名': district_counts.index,
        '销售数量': district_counts.values
    })

    # 将结果保存为 CSV 文件
    output_file_path = "district_house_sum.csv"
    result_df.to_csv(output_file_path, encoding='utf-8', index=False)

    print(f"结果已保存到 {output_file_path}")



def get_monthly_average_price():
    # 确保 '合同签订日期' 列是日期类型
    df['合同签订日期'] = pd.to_datetime(df['合同签订日期'])

    # 计算每个月的平均计划出售单价
    monthly_avg = df.groupby(df['合同签订日期'].dt.to_period('M'))['计划出售单价'].mean()

    # 将结果转换为 DataFrame
    result_df = monthly_avg.to_frame().reset_index()
    result_df.columns = ['月份', '平均计划出售单价']

    # 将结果保存为 CSV 文件
    output_file_path = "monthly_average_price.csv"
    result_df.to_csv(output_file_path, encoding='utf-8', index=False)

    print(f"结果已保存到 {output_file_path}")


def get_use_sum():
    # 统计每个区的数据数量，包括空值
    district_counts = df['用途'].value_counts(dropna=False)

    # 将空值替换为一个明确的标签，例如 '无'
    district_counts.index = district_counts.index.fillna('空值')

    # 创建一个新的 DataFrame，包含两列：'区名' 和 '销售数量'
    result_df = pd.DataFrame({
        '用途': district_counts.index,
        '数量': district_counts.values
    })

    # 将结果保存为 CSV 文件
    output_file_path = "use_house_sum.csv"
    result_df.to_csv(output_file_path, encoding='utf-8', index=False)

    print(f"结果已保存到 {output_file_path}")


def get_price_count():
    # 确定价格区间
    price_range = list(range(0, 950001, 2500))

    # 初始化统计对象
    count_by_range = {price: 0 for price in price_range}

    # 遍历数据并统计
    for price in df['计划出售单价']:
        for i, upper_bound in enumerate(price_range):
            if price < upper_bound:
                count_by_range[price_range[i]] += 1
                break

    # 创建一个新的 DataFrame，包含两列：'价格区间' 和 '数量'
    result_df = pd.DataFrame({
        '价格区间': [f'{price}-{upper_bound}' for price, upper_bound in zip(price_range[:-1], price_range[1:])],
        '数量': [count_by_range[price] for price in price_range[:-1]]
    })

    # 将结果保存为 CSV 文件
    output_file_path = "price_count2.csv"
    result_df.to_csv(output_file_path, encoding='utf-8', index=False)

    print(f"结果已保存到 {output_file_path}")


def get_yearly_sales():
    # 提取年份
    df['签订年份'] = pd.to_datetime(df['合同签订日期']).dt.year

    # 统计每年售出的房子数量
    yearly_counts = df['签订年份'].value_counts().sort_index()

    # 创建一个新的 DataFrame，包含两列：'年份' 和 '销售数量'
    result_df = pd.DataFrame({
        '年份': yearly_counts.index,
        '销售数量': yearly_counts.values
    })

    # 将结果保存为 CSV 文件
    output_file_path = "yearly_sales.csv"
    result_df.to_csv(output_file_path, encoding='utf-8', index=False)

    print(f"结果已保存到 {output_file_path}")


# 调用函数
get_yearly_sales()