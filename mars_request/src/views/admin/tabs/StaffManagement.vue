<template>
  <div class="flex flex-col gap-6">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
      <h1 class="text-2xl md:text-3xl font-extrabold text-[#333] tracking-tight">Staff Management</h1>
      <button @click="$emit('open-staff-modal')" class="px-6 py-2.5 bg-[#004d66] text-white font-bold rounded hover:bg-[#003d52] transition-colors shadow-md flex items-center gap-2">
        <component :is="UserIcon" class="w-5 h-5" /> Add New Staff
      </button>
    </div>

    <div class="bg-white rounded-lg shadow-sm border border-[#e2e8f0] overflow-hidden">
      <table class="w-full text-left border-collapse">
        <thead>
          <tr class="bg-slate-50 border-b-2 border-[#333]">
            <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest">Full Name</th>
            <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest">Username</th>
            <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest">Staff ID</th>
            <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest">Department</th>
            <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest text-center">Action</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-200">
          <tr v-if="staffList.length === 0" class="p-20 text-center"><td colspan="5" class="py-20 italic text-slate-400">No staff records found.</td></tr>
          <tr v-for="stf in staffList" :key="stf.id" class="hover:bg-slate-50 transition-colors">
            <td class="px-6 py-4 font-bold text-[#00334d]">{{ stf.full_name }}</td>
            <td class="px-6 py-4 text-sm text-slate-600">@{{ stf.username }}</td>
            <td class="px-6 py-4 text-sm font-mono">{{ stf.staff_id }}</td>
            <td class="px-6 py-4 text-sm font-semibold text-slate-500">{{ stf.department }}</td>
            <td class="px-6 py-4 text-center flex justify-center gap-2">
              <button @click="$emit('edit-staff', stf)" class="p-2 text-cyan-600 hover:bg-cyan-50 rounded transition-colors">
                <component :is="CogIcon" class="w-5 h-5" />
              </button>
              <button @click="$emit('delete-staff', stf.id)" class="p-2 text-red-600 hover:bg-red-50 rounded transition-colors">
                <component :is="XIcon" class="w-5 h-5" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { User as UserIcon, Settings as CogIcon, X as XIcon } from 'lucide-vue-next';

defineProps({
  staffList: Array
});

defineEmits(['open-staff-modal', 'edit-staff', 'delete-staff']);
</script>
