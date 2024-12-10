// 饼图数据 (充电桩饱和比例) //已改
export const chargingPileData = [
  {
    value: 179697,
    name: "历城区",
    percentage: "31.5%",
    color: "#8A00E1",
  },
  {
    value: 52635,
    name: "历下区",
    percentage: "9.2%",
    color: "#34D160",
  },
  {
    value: 30940,
    name: "长清区",
    percentage: "5.4%",
    color: "#027FF2",
  },
  {
    value: 44279,
    name: "槐荫区",
    percentage: "7.7%",
    color: "#F19610",
  },
  {
    value: 40859,
    name: "市中区",
    percentage: "7.1%",
    color: "#6054FF",
  },
  {
    value: 221492,
    name: "其他",
    percentage: "39.1%",
    color: "#00C6FF",
  }
]

// 折线图 (流程监控)
export const processMonitoringData = [
    {
    name: "2020",
    data: [8985, 9504, 8977, 10156, 9649, 9634, 10121, 9149, 9264, 9063, 9154, 11437]
  },
  {
    name: "2019",
    data: [9304, 10356, 10840, 10488, 10339, 10505, 10401, 10115, 9333, 9444, 9507, 9505]
  }
]

// 柱状图 (充电数据统计)
export const chargingStatisticsData = 
[
  {
    name:"0.25-5",
    value:50638
  },
    {
    name:"5-0.75",
    value:115356
  },
    {
    name:"0.75-1",
    value:93644
  },
    {
    name:"1-1.25",
    value:76883
  },
    {
    name:"1.25-1.5",
    value:61039
  },
    {
    name:"1.5-1.75",
    value:68675
  },
    {
    name:"1.75-2",
    value:40820
  },
    {
    name:"2-2.25",
    value:18209
  },
    {
    name:"2.25-2.5",
    value:15560
  },
    {
    name:"2.5-2.75",
    value:11292
  },
    {
    name:"2.75-3",
    value:6762
  },
    {
    name:"3-3.25",
    value:4676
  },
    {
    name:"3.25-3.5(万)",
    value:2619
  },
]

// 异常监控
export const exceptionMonitoringData = [
  {
    id: 1,
    name: "异常1",
    value: 5,
    dur: "10s",
    begin: "0s"
  },
  {
    id: 2,
    name: "异常2",
    value: 3,
    dur: "10s",
    begin: "-3s"
  },
  {
    id: 2,
    name: "异常3",
    value: 5,
    dur: "10s",
    begin: "-5s"
  }
]

// 充电桩数据分析
export const dataAnalysisData = [
  {
    id: 1,
    title: "19年交易量",
    totalNum: 14.5,
    unit: "万",
    percentage: 0,
    isUp: true,
  },
  {
    id: 2,
    title: "20年交易量",
    totalNum: 16.2,
    unit: "万",
    percentage: "11.9%",
    isUp: true,
  },
  {
    id: 3,
    title: "21年交易量",
    totalNum: 19.4,
    unit: "万",
    percentage: "19.7",
    isUp: true,
  }
]

export const chargingTop4Data = [
  {
    id: 1,
    name: "住宅",
    percentage: "56.5%",
  },
  {
    id: 2,
    name: "储藏室",
    percentage: "25.1%",
  },
  {
    id: 3,
    name: "车库",
    percentage: "7.9%",
  },
  {
    id: 4,
    name: "办公",
    percentage: "5.1%",
  },
  {
    id: 5,
    name: "商店",
    percentage: "3.8%",
  }
]

//右上水球
export const waterTotalData = 98.4