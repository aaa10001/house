<!-- Modal.vue -->
<template>
  <div v-if="visible" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <span class="close-button" @click="closeModal">&times;</span>
      <p>{{ info }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  info: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['close']);

function closeModal() {
  emit('close');
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  max-width: 300px;
  text-align: center;
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 20px;
}
</style>