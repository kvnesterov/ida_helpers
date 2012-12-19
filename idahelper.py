def EnumProc():
	ret = []
	for i in xrange(GetProcessQty()):
		pinfo = idaapi.process_info_t()
		pid = idaapi.get_process_info(i, pinfo)
		ret.append((pid, pinfo.name))
	return ret

def ShowProcList():
	for i in xrange(GetProcessQty()):
		pinfo = idaapi.process_info_t()
		pid = idaapi.get_process_info(i, pinfo)
		print("Pid: " + str(pid) + ", Name: " + pinfo.name)

def FindNameByPid(search_pid):
	for i in xrange(GetProcessQty()):
		pinfo = idaapi.process_info_t()
		pid = idaapi.get_process_info(i, pinfo)
		if search_pid == pid:
			return pinfo.name

	raise AttributeError("No such pid.")

def FindFirstPidByName(search_name):
	for i in xrange(GetProcessQty()):
		pinfo = idaapi.process_info_t()
		pid = idaapi.get_process_info(i, pinfo)
		name = pinfo.name[:pinfo.name.index('\x00')] # Get clear string
		if search_name.lower() == name.lower():
			return pid
	
	raise AttributeError("No such proc name.")
