<template>
  <div class="flex flex-col gap-8">
    <!-- Page Header & Search -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
      <h1 class="text-2xl md:text-3xl font-extrabold text-[#333] tracking-tight">Record Requests</h1>
      <div class="flex flex-col sm:flex-row gap-2">
        <div class="relative w-full sm:w-auto">
          <input 
            type="text" 
            placeholder="Search Passkey, name, email or LRN..." 
            v-model="searchQuery"
            @input="onSearch"
            class="w-full sm:w-[280px] py-2.5 px-4 pr-10 bg-white border border-[#e2e8f0] rounded text-[0.95rem] focus:outline-none focus:ring-2 focus:ring-[#004d66]/10 focus:border-[#004d66] transition-all"
          />
          <SearchIcon class="absolute right-3 top-2.5 w-5 h-5 text-slate-400" />
        </div>
        
        <select v-model="strandFilter" @change="loadRequests" class="py-2.5 px-4 bg-white border border-[#e2e8f0] rounded text-[0.85rem] font-bold text-[#00334d] outline-none">
          <option value="">All Strands</option>
          <option v-for="s in strands" :key="s.id" :value="s.id">{{ s.name }}</option>
        </select>

        <select v-model="yearFilter" @change="loadRequests" class="py-2.5 px-4 bg-white border border-[#e2e8f0] rounded text-[0.85rem] font-bold text-[#00334d] outline-none">
          <option value="">All Years</option>
          <option v-for="y in Array.from({length: 11}, (_, i) => 2020 + i)" :key="y" :value="y">{{ y }}</option>
        </select>
      </div>
    </div>

    <!-- Filters Bar -->
    <div class="flex flex-wrap items-center gap-3">
      <button 
        v-for="s in statusFilters" 
        :key="s.value"
        @click="setFilter(s.value)"
        :class="[
          'px-6 py-2 rounded font-bold text-sm transition-all border shadow-sm',
          statusFilter === s.value 
            ? 'bg-[#00334d] text-white border-[#00334d]' 
            : 'bg-white text-slate-600 border-slate-200 hover:border-slate-300'
        ]"
      >
        {{ s.label }}
      </button>
    </div>

    <!-- Table Content -->
    <div class="bg-white rounded-lg shadow-sm border border-[#e2e8f0] overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-slate-50 border-b-2 border-[#333]">
              <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest border-r border-slate-200">Date Applied</th>
              <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest border-r border-slate-200 min-w-[200px]">Student Name</th>
              <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest border-r border-slate-200">Status</th>
              <th class="px-6 py-4 text-[0.75rem] font-black text-slate-700 uppercase tracking-widest text-center">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
            <tr v-if="loading" class="text-center">
              <td colspan="4" class="py-20 text-slate-400 italic">Fetching request records...</td>
            </tr>
            <tr v-else-if="requests.length === 0" class="text-center">
              <td colspan="4" class="py-20 text-slate-400 italic">No records found.</td>
            </tr>
            <tr v-for="req in requests" :key="req.id" class="hover:bg-slate-50 transition-colors">
              <td class="px-6 py-5 text-[0.85rem] font-medium text-slate-500 border-r border-slate-100 italic">{{ formatDate(req.submitted_at) }}</td>
              <td class="px-6 py-5 border-r border-slate-100">
                <div class="flex flex-col">
                  <div class="flex items-center gap-2">
                    <span class="px-2 py-0.5 bg-slate-100 text-[0.6rem] font-black text-slate-500 rounded uppercase tracking-tighter">{{ req.passkey }}</span>
                    <span class="text-[0.95rem] font-bold text-[#00334d]">{{ req.first_name }} {{ req.last_name }}</span>
                    <AttachmentIcon v-if="req.documents?.length > 0" class="w-3.5 h-3.5 text-amber-500" />
                  </div>
                  <span class="text-[0.7rem] text-slate-400 tracking-wider font-semibold">{{ req.strand_display || req.strand || 'No Strand' }}</span>
                </div>
              </td>
              <td class="px-6 py-5 border-r border-slate-100 text-center">
                <span class="px-3 py-1 rounded-full text-[0.65rem] font-black uppercase tracking-wider" :class="statusClass(req.status)">
                  {{ req.status }}
                </span>
              </td>
              <td class="px-6 py-5 text-center">
                <button @click="$emit('open-request', req)" class="px-8 py-2 bg-[#ffde59] border-2 border-[#333] rounded font-bold text-sm text-[#333] hover:bg-white transition-all shadow-sm uppercase tracking-wide">
                  Details
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { adminService } from '@/services/api';
import { Search as SearchIcon, Paperclip as AttachmentIcon } from 'lucide-vue-next';

const requests = ref([]);
const strands = ref([]);
const loading = ref(false);
const searchQuery = ref('');
const statusFilter = ref('');
const strandFilter = ref('');
const yearFilter = ref('');

const statusFilters = [
  { label: 'All', value: '' },
  { label: 'Pending', value: 'Pending' },
  { label: 'Approved', value: 'Approved' },
  { label: 'Completed', value: 'Completed' },
];

const loadRequests = async () => {
  loading.value = true;
  try {
    const params = {};
    if (statusFilter.value) params.status = statusFilter.value;
    if (searchQuery.value.trim()) params.search = searchQuery.value.trim();
    if (strandFilter.value) params.strand = strandFilter.value;
    if (yearFilter.value) params.year = yearFilter.value;
    const res = await adminService.getRequests(params);
    requests.value = res.data;
  } catch (err) { console.error('Requests error:', err); }
  finally { loading.value = false; }
};

const loadStrands = async () => {
  try {
    const res = await adminService.getStrands();
    strands.value = res.data;
  } catch (err) { console.error('Strands error:', err); }
};

let searchTimeout = null;
const onSearch = () => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(loadRequests, 350);
};

const setFilter = (val) => {
  statusFilter.value = val;
  loadRequests();
};

const formatDate = (dt) => dt ? new Date(dt).toLocaleDateString('en-PH', { year: 'numeric', month: 'short', day: 'numeric' }) : '—';
const statusClass = (s) => ({
  'bg-amber-100 text-amber-600 border border-amber-200': s === 'Pending',
  'bg-orange-100 text-orange-600 border border-orange-200': s === 'Needs Verification',
  'bg-green-100 text-green-600 border border-green-200': s === 'Approved',
  'bg-purple-100 text-purple-600 border border-purple-200': s === 'Completed',
  'bg-red-100 text-red-600 border border-red-200': s === 'Rejected',
});

onMounted(() => {
  loadRequests();
  loadStrands();
});

// Expose refresh function to parent
defineExpose({ refresh: loadRequests });
</script>
