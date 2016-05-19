__author__ = 'Nelson'

from slab.experiments.ExpLib.SequentialExperiment import *
from slab.experiments.General.run_seq_experiment import *
from slab import *
import os
import json


datapath = os.getcwd() + '\data'
config_file = os.path.join(datapath, "..\\config" + ".json")
with open(config_file, 'r') as fid:
        cfg_str = fid.read()

cfg = AttrDict(json.loads(cfg_str))

def get_data_filename(prefix):
    return  os.path.join(datapath, get_next_filename(datapath, prefix, suffix='.h5'))


def multimode_pulse_calibration(seq_exp, mode):
    # pulse_calibration(seq_exp)
    seq_exp.run('multimode_calibrate_offset',{'exp':'multimode_rabi','dc_offset_guess':0,'mode':mode,'update_config':True})

def multimode_dc_offset_recalibration(seq_exp, mode):
    # pulse_calibration(seq_exp)
    seq_exp.run('multimode_calibrate_offset',{'exp':'long_multimode_ramsey','dc_offset_guess':cfg['multimodes'][mode]['dc_offset_freq'],'mode':mode,'update_config':True})

def multimode_ef_pulse_calibration(seq_exp, mode):
    # pulse_calibration(seq_exp)
    seq_exp.run('multimode_calibrate_ef_sideband',{'exp':'multimode_ef_rabi','dc_offset_guess_ef':0,'mode':mode,'update_config':True})

def multimode_pi_pi_phase_calibration(seq_exp,mode):
    seq_exp.run('multimode_pi_pi_experiment',{'mode':mode,'update_config':True})

def multimode_ef_dc_offset_recalibration(seq_exp, mode):
    # pulse_calibration(seq_exp)
    seq_exp.run('multimode_calibrate_ef_sideband',{'exp':'long_multimode_ef_ramsey','dc_offset_guess_ef':cfg['multimodes'][mode]['dc_offset_freq_ef'],'mode':mode,'update_config':True})


def multimode_ge_calibration_all(seq_exp, kwargs):
    frequency_stabilization(seq_exp)
    multimode_pulse_calibration(seq_exp, kwargs['mode'])
    multimode_dc_offset_recalibration(seq_exp, kwargs['mode'])
    multimode_pi_pi_phase_calibration(seq_exp, kwargs['mode'])


def multimode_cz_calibration(seq_exp, mode):
    pulse_calibration(seq_exp)
    multimode_pulse_calibration(seq_exp, mode)
    ef_frequency_calibration(seq_exp)
    ef_pulse_calibration(seq_exp)
    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment',
                {'mode': mode, 'offset_exp': 0, 'update_config': True})
    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment',
                {'mode': mode, 'offset_exp': 1, 'update_config': True})

def multimode_cz_2modes_calibration(seq_exp, mode, mode2, data_file_2):


    frequency_stabilization(seq_exp)
    # pulse_calibration(seq_exp)
    #
    # multimode_pulse_calibration(seq_exp, mode)
    # multimode_pulse_calibration(seq_exp, mode2)
    # multimode_pi_pi_phase_calibration(seq_exp,mode2)

    ef_frequency_calibration(seq_exp)
    # ef_pulse_calibration(seq_exp)

    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment',
                {'mode': mode, 'offset_exp': 0, 'update_config': True, "data_file": data_file_2})
    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment',
                {'mode': mode, 'offset_exp': 1, 'update_config': True, "data_file": data_file_2})

    seq_exp.run('multimode_mode_mode_cz_v2_offset_experiment',
                {'mode': mode, 'mode2': mode2, 'offset_exp': 0, 'update_config': True, "data_file": data_file_2})
    seq_exp.run('multimode_mode_mode_cz_v2_offset_experiment',
                {'mode': mode, 'mode2': mode2, 'offset_exp': 1, 'update_config': True, "data_file": data_file_2})


def multimode_cz_test(seq_exp, mode ,data_file ):
    multimode_cz_calibration(seq_exp, mode)
    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment', {'mode': mode
        , 'offset_exp': 3, 'load_photon': False, "data_file": data_file})
    seq_exp.run('multimode_qubit_mode_cz_v2_offset_experiment', {'mode': mode
        , 'offset_exp': 3, 'load_photon': True, "data_file": data_file})


def multimode_cz_2modes_test(seq_exp, mode, mode2 ,data_file,data_file_2 ):
    multimode_cz_2modes_calibration(seq_exp, mode, mode2,data_file_2)

    seq_exp.run('multimode_mode_mode_cz_v2_offset_experiment',
                {'mode': mode, 'mode2': mode2, 'offset_exp': 3, 'load_photon': False, 'update_config': True, "data_file": data_file})
    seq_exp.run('multimode_mode_mode_cz_v2_offset_experiment',
                {'mode': mode, 'mode2': mode2, 'offset_exp': 3, 'load_photon': True, 'update_config': True, "data_file": data_file})


def run_multimode_seq_experiment(expt_name,lp_enable=True,**kwargs):
    seq_exp = SequentialExperiment(lp_enable)
    prefix = expt_name.lower()
    data_file = get_data_filename(prefix)

    if expt_name.lower() == 'multimode_pulse_calibration':
        multimode_pulse_calibration(seq_exp,kwargs['mode'])

    if expt_name.lower() == 'multimode_ef_pulse_calibration':
        multimode_ef_pulse_calibration(seq_exp,kwargs['mode'])

    if expt_name.lower() == 'multimode_ef_dc_offset_calibration':
        multimode_ef_dc_offset_recalibration(seq_exp,kwargs['mode'])

    if expt_name.lower() == 'multimode_dc_offset_calibration':
        multimode_dc_offset_recalibration(seq_exp,kwargs['mode'])

    if expt_name.lower() == 'multimode_pi_pi_phase_calibration':
        multimode_pi_pi_phase_calibration(seq_exp,kwargs['mode'])

    if expt_name.lower() == 'multimode_cphase_calibration':

        pulse_calibration(seq_exp)
        multimode_pulse_calibration(seq_exp,mode=kwargs['mode'])
        multimode_dc_offset_recalibration(seq_exp,mode=kwargs['mode'])
        multimode_ef_pulse_calibration(seq_exp,mode=kwargs['mode'])
        multimode_ef_dc_offset_recalibration(seq_exp,mode=kwargs['mode'])
        multimode_pulse_calibration(seq_exp,mode=kwargs['mode2'])
        multimode_pi_pi_phase_calibration(seq_exp,mode=kwargs['mode2'])

        for i in arange(4):
            frequency_stabilization(seq_exp)
            seq_exp.run('multimode_qubit_mode_cz_offset_experiment',{'mode':kwargs['mode'],'mode2':kwargs['mode2'],'offset_exp':0,'load_photon':0,'update_config':True})
            seq_exp.run('multimode_qubit_mode_cz_offset_experiment',{'mode':kwargs['mode'],'mode2':kwargs['mode2'],'offset_exp':1,'load_photon':0,'update_config':True})
            for offset_exp in arange(2,4):
                for load_photon in arange(2):
                    frequency_stabilization(seq_exp)
                    seq_exp.run('multimode_qubit_mode_cz_offset_experiment',{'mode':kwargs['mode'],'mode2':kwargs['mode2'],'offset_exp':offset_exp,'load_photon':load_photon,'update_config':True})


    if expt_name.lower() == 'sequential_state_dep_shift_calibration':
        modelist = array([1,3,4,5,6,9])
        for mode in modelist:
            pulse_calibration(seq_exp,phase_exp=False)
            seq_exp.run('multimode_state_dep_shift',{'mode':mode,'exp':0,'qubit_shift_ge':0,'qubit_shift_ef':1,'update_config':True})

    if expt_name.lower() == 'cphase_segment_tests':
        modelist = array([4])
        pulse_calibration(seq_exp,phase_exp=True)
        multimode_pi_pi_phase_calibration(seq_exp,mode=6)
        multimode_ef_pulse_calibration(seq_exp,mode=4)
        for j in arange(3):
            for mode in modelist:
                for subexp in arange(5):
                    seq_exp.run('multimode_state_dep_shift',{'mode':mode,'mode2':6,'exp':6,'qubit_shift_ge':0,'qubit_shift_ef':1,'subexp':subexp,'update_config':True})
                    frequency_stabilization(seq_exp)

    if expt_name.lower() == 'sequential_state_dep_pulse_phase_calibration':
        modelist = array([6])

        pulse_calibration(seq_exp)
        multimode_pulse_calibration(seq_exp,mode=6)
        multimode_pi_pi_phase_calibration(seq_exp,mode=6)
        multimode_ef_pulse_calibration(seq_exp,mode=4)
        for j in arange(3):
            for mode in modelist:
                for load_photon in arange(2):
                    seq_exp.run('multimode_state_dep_shift',{'mode':mode,'mode2':4,'exp':5,'qubit_shift_ge':1,'qubit_shift_ef':0,'load_photon':load_photon,'update_config':True})
                    frequency_stabilization(seq_exp)
            # seq_exp.run('multimode_state_dep_shift',{'mode':mode,'exp':3,'update_config':True})
            # seq_exp.run('multimode_state_dep_shift',{'mode':mode,'exp':4,'update_config':True})


    if expt_name.lower() == 'multimode_cz_calibration':
        multimode_cz_calibration(seq_exp, kwargs['mode'])

    if expt_name.lower() == 'multimode_cz_2modes_calibration':
        multimode_cz_2modes_calibration(seq_exp, kwargs['mode'],kwargs['mode2'])


    if expt_name.lower() == 'multimode_cz_test':
        multimode_cz_test(seq_exp, kwargs['mode'], data_file)

    if expt_name.lower() == 'multimode_cz_2modes_test':
        multimode_cz_2modes_test(seq_exp, kwargs['mode'],kwargs['mode2'], data_file)

    if expt_name.lower() == 'sequential_multimode_cz_test':
        modelist = array([1,5,6,9])
        for mode in modelist:
            multimode_cz_test(seq_exp, mode, data_file)


    if expt_name.lower() == 'sequential_multimode_cz_2modes_test':

        data_file_2 = get_data_filename("sequential_multimode_cz_2modes_calibration")

        modelist = array([1,5,6,9])
        for mode in modelist:
            for mode2 in modelist:
                if not mode == mode2:
                    multimode_cz_2modes_test(seq_exp, mode, mode2, data_file, data_file_2)



    if expt_name.lower() == 'multimode_ge_calibration_all':
        multimode_ge_calibration_all(seq_exp,kwargs)

    if expt_name.lower() == 'multimode_ef_calibration_all':
        multimode_ef_pulse_calibration(seq_exp,kwargs['mode'])
        multimode_ef_dc_offset_recalibration(seq_exp,kwargs['mode'])


    if expt_name.lower() == 'sequential_multimode_calibration':

        modelist = array([1,3,4,5,6,9])
        for mode in modelist:
            pulse_calibration(seq_exp)
            multimode_pulse_calibration(seq_exp,mode)
            multimode_dc_offset_recalibration(seq_exp,mode)
            multimode_ef_pulse_calibration(seq_exp,mode)
            multimode_ef_dc_offset_recalibration(seq_exp,mode)
            multimode_pi_pi_phase_calibration(seq_exp,mode)


    if expt_name.lower() == 'sequential_dc_offset_recalibration':
        modelist = array([1,3,4,5,6,9])
        pulse_calibration(seq_exp)
        for i in arange(len(modelist)):
            multimode_dc_offset_recalibration(seq_exp,modelist[i])
            multimode_ef_dc_offset_recalibration(seq_exp,modelist[i])


    if expt_name.lower() == 'multimode_rabi_scan':

        freqlist = array([2.19257e9,2.292e9,2.362089e9,2.546e9, 2.725e9,2.895e9])
        freqspan = linspace(-1,29,30)
        amplist = array([1,1,1,1,1,1])
        modelist = array([1,3,4,5,6,9])

        for i in arange(len(modelist)):
            frequency_stabilization(seq_exp)
            print "running Rabi sweep around mode %s"%(modelist[i])
            for freq in freqspan:
                flux_freq = freqlist[i] + freq*1e6
                seq_exp.run('multimode_rabi_sweep',{'flux_freq':flux_freq,'amp':amplist[i],"data_file":data_file})


    if expt_name.lower() == 'multimode_ef_rabi_scan':

        # freqlist = array([2.58e9,2.942e9,3.116e9])
        # freqspan = linspace(-7,7,15)
        # amplist = array([0.4,0.8,0.65])
        # modelist = array([4,6,9])
        #
        #
        freqlist = array([2.414e9,2.514e9,2.583e9,2.762e9,2.946e9,3.116e9])
        freqspan = linspace(-1,29,30)
        amplist = array([1,1,1,1,1,1])
        modelist = array([1,3,4,5,6,9])

        # freqlist = array([2.514e9,2.762e9])
        # freqspan = linspace(-9,10,20)
        # amplist = array([0.65,0.65])
        # modelist = array([3,5])

        for i in arange(len(modelist)):
            frequency_stabilization(seq_exp)
            print "running ef Rabi sweep around mode %s"%(modelist[i])
            for freq in freqspan:
                flux_freq = freqlist[i] + freq*1e6
                seq_exp.run('multimode_ef_rabi_sweep',{'flux_freq':flux_freq,'amp':amplist[i],"data_file":data_file})


    if expt_name.lower() == 'sequential_single_mode_rb':
        for i in arange(32):
            multimode_pulse_calibration(seq_exp,kwargs['mode'])
            multimode_pi_pi_phase_calibration(seq_exp,kwargs['mode'])
            seq_exp.run('single_mode_rb',{'mode':kwargs['mode'],"data_file":data_file})



    if expt_name.lower() == 'sequential_cphase_amplification':
        mode1 = 6
        mode2 = 1
        multimode_pulse_calibration(seq_exp,mode1)
        multimode_ef_pulse_calibration(seq_exp,mode2)
        multimode_pi_pi_phase_calibration(seq_exp,mode1)
        multimode_ef_dc_offset_recalibration(seq_exp,mode2)
        for i in arange(0,15):
            frequency_stabilization(seq_exp)
        seq_exp.run('multimode_ef_pi_pi_experiment',{'mode_1':mode1,'mode_2':mode2,'update_config':True})
        seq_exp.run('multimode_cphase_amplification',{'mode_1':mode1,'mode_2':mode2,'number':i,"data_file":data_file})

    if expt_name.lower() == 'sequential_cnot_amplification':
        mode1 = 6
        mode2 = 4
        multimode_pulse_calibration(seq_exp,mode1)
        multimode_ef_pulse_calibration(seq_exp,mode2)
        multimode_pi_pi_phase_calibration(seq_exp,mode1)
        multimode_ef_dc_offset_recalibration(seq_exp,mode2)
        for i in arange(0,12,1):
            frequency_stabilization(seq_exp)
            seq_exp.run('multimode_cnot_amplification',{'mode_1':mode1,'mode_2':mode2,'number':i,"data_file":data_file})


    if expt_name.lower() == 'cphase_amplification':
        mode1 = 6
        mode2 = 1
        seq_exp.run('multimode_ef_pi_pi_experiment',{'mode_1':mode1,'mode_2':mode2,'update_config':True})
        seq_exp.run('multimode_cphase_amplification',{'mode_1':mode1,'mode_2':mode2,'number':15})


