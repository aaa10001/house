<template>
  <div ref="divRef" :style="{ width, height }"></div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue"
import useEcharts from "../hooks/useEcharts"

const props = defineProps({
  width: {
    type: String,
    default: "100%"
  },
  height: {
    type: String,
    default: "100%"
  },
  echartDatas: {
    type: Array,
    default: () => []
  }
})

// 监听echartDatas的变化
watch(() => props.echartDatas, (newValue) => {
  setupEchart(newValue)
})

let divRef = ref(null)
let hyChart = null
onMounted(() => {
  setupEchart(props.echartDatas)
})

function setupEchart(echartDatas) {
  if (!hyChart) {
    hyChart = useEcharts(divRef.value)
  }
  let option = getOption(echartDatas)
  hyChart.setOption(option)
}

// 配置项
function getOption(echartDatas) {
  const allData = echartDatas.flatMap(item => item.data);
  const minVal = Math.min(...allData);
  const maxVal = Math.max(...allData);

  return {
    grid: {
      left: "5%",
      right: "1%",
      top: "20%",
      bottom: "15%",
      containLabel: true
    },
    legend: {
      right: "center",
      bottom: "5%",
      itemGap: 20,
      itemWidth: 13,
      itemHeight: 12,
      textStyle: {
        color: "#64BCFF"
      },
      icon: "rect"
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "line",
        lineStyle: {
          color: "#20FF89"
        }
      }
    },
    xAxis: [
      {
        type: "category",
        axisLine: {
          show: false
        },
        axisLabel: {
          color: "#64BCFF"
        },
        splitLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        data: [
          "1月",
          "2月",
          "3月",
          "4月",
          "5月",
          "6月",
          "7月",
          "8月",
          "9月",
          "10月",
          "11月",
          "12月"
        ]
      }
    ],
    yAxis: [
      {
        type: "value",
        splitLine: {
          show: false
        },
        axisLine: {
          show: false
        },
        axisLabel: {
          show: true,
          color: "#64BCFF"
        },
        min: minVal - 500, // 略低于最小值
        max: maxVal + 500  // 略高于最大值
      }
    ],
    series: echartDatas.map((item, index) => {
      if (!item || !item.name || !Array.isArray(item.data)) {
        console.error(`Invalid data at index ${index}:`, item);
        return null;
      }
      return {
        name: item.name,
        type: "line",
        smooth: true,
        symbolSize: 5,
        showSymbol: false,
        itemStyle: {
          color: getColorForSeries(index),
          lineStyle: {
            color: getColorForSeries(index),
            width: 2
          }
        },
        areaStyle: {
          color: {
            type: "linear",
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              {
                offset: 0,
                color: getColorForSeries(index)
              },
              {
                offset: 1,
                color: "rgba(255, 255, 255, 0)"
              }
            ]
          }
        },
        data: item.data
      };
    }).filter(Boolean) // 过滤掉无效的系列
  };

  function getColorForSeries(index) {
    const colors = ["#20FF89", "#EA9502", "#FF6D6D"]; // 定义一系列颜色
    return colors[index % colors.length]; // 循环使用这些颜色
  }
}
</script>

<style scoped></style>