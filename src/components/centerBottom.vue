<template>
  <div class="bottom-content">
    <template v-for="(item, index) in panelItems" :key="item.id">
      <div :class="['item', `panel${item.id}`]">
        <div class="pan-left">
          <div class="title">{{ item.title }}</div>
          <!-- 数据动画 -->
          <span :id="`total-num-${item.id}`" class="number">{{ item.totalNum }}</span>
          <span class="unit">{{ item.unit }}</span>
        </div>
        <div class="pan-right">
          <span
            :class="[
              'triangle',
              item.isUp ? 'up-triangle' : 'down-triangle',
              item.isUp ? 'green' : 'red'
            ]"
          ></span>
          <!-- 百分比动画 -->
          <span
            :id="`percentage-num-${item.id}`"
            class="percentage"
            :class="{ green: item.isUp, red: !item.isUp }"
          >{{ item.percentage }}</span>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { watch, nextTick } from "vue";
import { CountUp } from "countup.js";

const props = defineProps({
  panelItems: {
    type: Array,
    default: () => []
  }
})

watch(() => props.panelItems, () => {
  nextTick(() => {
    const option1 = {
      decimalPlaces: 1,    // 保留一位小数
      duration: 2,         // 动画时长
      useGrouping: false   // 是否分组 1000 -> 1,000 这种形式
    }
    const option2 = {
      ...option1,          // 继承 option1 的配置
      suffix: "%"          // 添加百分比后缀
    }
    
    props.panelItems.forEach(item => {
      new CountUp(`total-num-${item.id}`, item.totalNum, option1).start()
      new CountUp(`percentage-num-${item.id}`, item.percentage, option2).start()
    })
  })
})
</script>

<style scoped lang="scss">
.bottom-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;

  .item {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 60px;
    flex: 1;
    height: 100%;
    padding: 0 10px 0 35px;

    .pan-left {
      font-size: 16px;
      color: #ffffff;
      opacity: 0.8;

      .title {
        color: white;
      }

      .number {
        font-size: 36px;
        font-weight: bold;
        color: #23aeff;
        line-height: 60px;
      }

      .unit {
        font-size: 18px;
        color: #23aeff;
      }
    }

    .pan-right {
      margin-top: 35px;

      .triangle {
        display: inline-block;
        margin-bottom: 4px;
        width: 0;
        height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;

        &.up-triangle {
          border-bottom: 8px solid; // 箭头向上
          &.green {
            border-bottom-color: #37a73f; // 绿色箭头
          }
          &.red {
            border-bottom-color: #ff4d4d; // 红色箭头
          }
        }

        &.down-triangle {
          border-top: 8px solid; // 箭头向下
          &.green {
            border-top-color: #37a73f; // 绿色箭头
          }
          &.red {
            border-top-color: #ff4d4d; // 红色箭头
          }
        }
      }

      .percentage {
        transition: color 0.3s ease; // 添加颜色过渡效果

        &.green {
          color: #37a73f; // 绿色
        }

        &.red {
          color: #ff4d4d; // 红色
        }
      }
    }
  }
}
</style>