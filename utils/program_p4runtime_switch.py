from p4runtime_switch import P4RuntimeSwitch
import sys, os, p4runtime_lib.simple_controller



grpc_port = int(sys.argv[1])
device_id = int(sys.argv[2])
runtime_json = sys.argv[3]
sw_name = sys.argv[4]
log_dir = sys.argv[5]

print('Configuring switch %s using P4Runtime with file %s' % (sw_name, runtime_json))
with open(runtime_json, 'r') as sw_conf_file:
	outfile = '%s/%s-p4runtime-requests.txt' %(log_dir, sw_name)
	p4runtime_lib.simple_controller.program_switch(addr='127.0.0.1:%d' % grpc_port, device_id=device_id, sw_conf_file=sw_conf_file, workdir=os.getcwd(), proto_dump_fpath=outfile)
