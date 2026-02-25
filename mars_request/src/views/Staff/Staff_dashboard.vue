<template>
  <div class="flex h-screen bg-[#f5f7fa] font-sans overflow-hidden">
    <!-- Sidebar -->
    <aside 
      :class="[
        'bg-[#00334d] text-white flex flex-col transition-all duration-300 ease-in-out z-40 shadow-xl',
        isSidebarExpanded ? 'w-64 fixed inset-y-0 left-0 translate-x-0' : 'w-20 md:w-20 -translate-x-full md:translate-x-0 md:static'
      ]"
    >
      <!-- Sidebar Nav -->
      <nav class="flex-grow pt-8 overflow-y-auto overflow-x-hidden">
        <ul class="flex flex-col">
          <li 
            v-for="item in menuItems" 
            :key="item.id"
            @click="currentView = item.id"
            :class="[
              'group flex items-center px-6 py-4 cursor-pointer transition-colors border-b border-white/5 relative',
              currentView === item.id ? 'bg-[#ffca28] text-[#0d324d]' : 'hover:bg-white/5'
            ]"
            :title="!isSidebarExpanded ? item.label : ''"
          >
            <div class="flex items-center min-w-[24px] justify-center">
              <component :is="item.icon" class="w-6 h-6 shrink-0" />
            </div>
            <span 
              :class="[
                'ml-4 font-semibold whitespace-nowrap transition-opacity duration-200',
                isSidebarExpanded ? 'opacity-100' : 'opacity-0 w-0 pointer-events-none'
              ]"
            >
              {{ item.label }}
            </span>
            <!-- Active Indicator for collapsed state -->
            <div v-if="!isSidebarExpanded && currentView === item.id" class="absolute left-0 w-1 h-full bg-[#0d324d]"></div>
          </li>
        </ul>
      </nav>

      <!-- Sidebar Footer / Logout -->
      <div class="p-6 border-t border-white/10">
        <button 
          @click="handleLogout" 
          class="w-full flex items-center justify-center p-2.5 rounded border border-white/30 text-white hover:bg-red-600 hover:border-red-600 transition-all duration-200 group"
          :title="!isSidebarExpanded ? 'Logout' : ''"
        >
          <LogOutIcon class="w-5 h-5 shrink-0" />
          <span 
            :class="[
              'ml-3 font-semibold transition-opacity duration-200',
              isSidebarExpanded ? 'opacity-100' : 'opacity-0 w-0 pointer-events-none'
            ]"
          >
            Logout
          </span>
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col min-w-0 overflow-hidden">
      <!-- Top Header -->
      <header class="h-20 bg-[#004d66] text-white flex items-center justify-between px-8 shadow-md z-10 shrink-0">
        <div class="flex items-center gap-6">
          <!-- Burger Menu Icon -->
          <button 
            @click="isSidebarExpanded = !isSidebarExpanded" 
            class="p-2 hover:bg-white/10 rounded transition-colors focus:outline-none"
            title="Toggle Sidebar"
          >
            <MenuIcon v-if="!isSidebarExpanded" class="w-7 h-7" />
            <XIcon v-else class="w-7 h-7" />
          </button>
          
          <div class="flex items-center gap-4 border-l border-white/20 pl-4 md:pl-6 h-10">
            <img :src="logoImg" alt="Logo" class="w-8 h-8 md:w-10 md:h-10 object-contain brightness-0 invert" />
            <div class="hidden xs:flex flex-col">
              <h2 class="text-[0.7rem] md:text-sm font-bold leading-tight uppercase tracking-wide">La Union Senior High School</h2>
              <p class="text-[0.6rem] md:text-[0.65rem] opacity-70 tracking-widest uppercase font-medium">Cabadbaran City</p>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-8">
          <div class="hidden md:flex flex-col text-right">
            <span class="text-xs font-medium opacity-90 italic">Welcome, {{ user?.full_name || 'Staff' }}</span>
            <span class="text-[0.7rem] font-bold uppercase tracking-wider text-amber-300 mt-0.5">{{ user?.department || 'Office' }}</span>
          </div>
          
          <div class="relative group cursor-pointer hover:opacity-80 transition-opacity">
            <BellIcon class="w-6 h-6" />
            <span class="absolute -top-1.5 -right-1.5 bg-[#ff4d4d] text-white text-[0.6rem] font-bold px-1.5 py-0.5 rounded-full border-2 border-[#004d66]">1</span>
          </div>
        </div>
      </header>

      <!-- Page Content Area -->
      <main class="flex-1 overflow-y-auto p-8 lg:p-12">
        <div class="max-w-7xl mx-auto">
          <!-- Page Header & Search -->
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-10">
            <h1 class="text-2xl md:text-3xl font-extrabold text-[#333] tracking-tight">Request List</h1>
            <div class="flex flex-col sm:flex-row gap-2">
              <div class="relative w-full sm:w-auto">
                <input 
                  type="text" 
                  placeholder="Search..." 
                  v-model="searchQuery"
                  class="w-full sm:w-[240px] md:w-[280px] py-2.5 px-4 pr-10 bg-white border border-[#e2e8f0] rounded text-[0.95rem] focus:outline-none focus:border-[#004d66] transition-all"
                />
                <SearchIcon class="absolute right-3 top-2.5 w-5 h-5 text-slate-400" />
              </div>
              <button class="w-full sm:w-auto px-6 py-2.5 border-2 border-[#1e293b] text-[#1e293b] font-bold rounded hover:bg-[#1e293b] hover:text-white transition-all duration-200 shadow-sm">
                Search
              </button>
            </div>
          </div>

          <!-- Filters Bar -->
          <div class="flex flex-col xl:flex-row justify-between gap-6 mb-6">
            <div class="flex items-center gap-4">
              <select v-model="statusFilter" class="w-[180px] py-2.5 px-4 bg-white border border-[#e2e8f0] rounded text-[0.95rem] font-medium focus:outline-none focus:border-[#004d66]">
                <option value="Pending">Pending</option>
                <option value="Approved">Approved</option>
                <option value="Completed">Completed</option>
              </select>
              <button class="px-8 py-2.5 bg-[#004d66] text-white font-bold rounded hover:bg-[#003d52] transition-colors shadow-sm">
                Select
              </button>
            </div>
            
            <div class="flex flex-wrap gap-2">
              <select v-for="n in 5" :key="n" class="py-2 px-4 bg-white border border-[#e2e8f0] rounded text-xs text-slate-600 focus:outline-none">
                <option>Lorem</option>
              </select>
            </div>
          </div>

          <!-- Table Content -->
          <div class="bg-white rounded-lg shadow-sm border border-[#e2e8f0] overflow-hidden">
            <div class="overflow-x-auto">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="bg-slate-50 border-b-2 border-[#333]">
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200 min-w-[200px]">Name</th>
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200">Lorem</th>
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200">Lorem</th>
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200">Lorem</th>
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200">Status</th>
                    <th class="px-6 py-4 text-[0.85rem] font-bold text-slate-700 uppercase tracking-wider">Action</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                  <tr v-for="request in dummyRequests" :key="request.id" class="hover:bg-slate-50 transition-colors">
                    <td class="px-6 py-5 text-[0.95rem] font-semibold text-slate-800 border-r border-slate-100">{{ request.name }}</td>
                    <td class="px-6 py-5 text-[0.9rem] text-slate-600 italic border-r border-slate-100">{{ request.lorem1 }}</td>
                    <td class="px-6 py-5 text-[0.9rem] text-slate-600 italic border-r border-slate-100">{{ request.lorem2 }}</td>
                    <td class="px-6 py-5 text-[0.9rem] text-slate-600 italic border-r border-slate-100">{{ request.lorem3 }}</td>
                    <td class="px-6 py-5 border-r border-slate-100">
                      <span class="font-bold text-[#1e293b]">{{ request.status }}</span>
                    </td>
                    <td class="px-6 py-5">
                      <button class="px-8 py-2 bg-[#ffde59] border border-[#333] rounded font-bold text-sm text-[#333] hover:bg-[#ffca28] transition-colors shadow-sm uppercase tracking-wide">
                        View
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, markRaw } from 'vue';
import { useRouter } from 'vue-router';
import { authService } from '@/services/api';
import logoImg from '@/assets/logo-launion.png';

// Lucide Icons (as raw components for use in loop)
import { 
  Menu as MenuIcon, 
  X as XIcon, 
  LayoutDashboard as DashboardIcon, 
  List as ListIcon, 
  Users as StudentIcon, 
  User as AccountIcon, 
  LogOut as LogOutIcon, 
  Bell as BellIcon,
  Search as SearchIcon
} from 'lucide-vue-next';

const router = useRouter();
const user = ref(null);
const isSidebarExpanded = ref(true);
const currentView = ref('request');
const searchQuery = ref('');
const statusFilter = ref('Pending');

const menuItems = [
  { id: 'dashboard', label: 'Dashboard', icon: markRaw(DashboardIcon) },
  { id: 'request', label: 'Request List', icon: markRaw(ListIcon) },
  { id: 'student', label: 'Student List', icon: markRaw(StudentIcon) },
  { id: 'account', label: 'My Account', icon: markRaw(AccountIcon) },
];

const dummyRequests = ref([
  { id: 1, name: 'John G. Doe Jr', lorem1: 'ipsum dolor sit amet', lorem2: 'ipsum dolor sit amet', lorem3: 'ipsum dolor sit amet', status: 'Pending' },
  { id: 2, name: 'John G. Doe Jr', lorem1: 'ipsum dolor sit amet', lorem2: 'ipsum dolor sit amet', lorem3: 'ipsum dolor sit amet', status: 'Pending' },
]);

onMounted(() => {
  const userData = localStorage.getItem('user');
  if (!userData) {
    router.push('/login');
    return;
  }
  user.value = JSON.parse(userData);
});

const handleLogout = () => {
  authService.logout();
  router.push('/login');
};
</script>

<style>
/* Global scrollbar styling for cleaner dashboard look */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>

