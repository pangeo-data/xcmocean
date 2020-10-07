import cmocean.cm as cmo
from collections import defaultdict

REGEX = {
    "temp": "temp|Celsius",
    "salt": "salt|salinity|psu",
    "vel": "u-momentum|u-velocity|v-momentum|v-velocity|vel|velocity|speed|u velocity|v velocity|m/s|meter second-1",
    "freq": "vort|vorticity|vertical_shear|dudz|dvdz|1/s|Coriolis",
    "zeta": "zeta|ssh|mld",
    "rho": "dense|density|kg/m^3",
    "energy": "energy|EKE|KE|PE|APE",
    "depths": "bathy|depths|bathymetry",
    "accel": "buoyancy|m/s^2|acceleration|dudt|dvdt|prsgrad",
    "freq2": "M2|N2|S2|1/s^2",
    "dye": "dye|concentration"
}

# sequential colormap defaults to viridis if variable type can't be determined
SEQ = defaultdict(lambda: cmo.cm.viridis)
SEQ.update({
    'temp': cmo.thermal,
    'salt': cmo.haline,
    'vel': cmo.speed,
    'freq': cmo.tempo,
    'zeta': cmo.amp,
    'rho': cmo.dense,
    'energy': cmo.speed,
    'depths': cmo.deep,
    'accel': cmo.rain,
    'freq2': cmo.rain,
    'dye': cmo.matter
})

# sequential colormap defaults to balance if variable type can't be determined
DIV = defaultdict(lambda: cmo.balance)
DIV.update({
    'temp': cmo.balance,
    'salt': cmo.diff,
    'vel': cmo.delta,
    'freq': cmo.curl,
    'zeta': cmo.balance,
    'rho': cmo.diff,
    'energy': cmo.delta,
    'depths': cmo.topo,
    'accel': cmo.tarn,
    'freq2': cmo.tarn,
    'dye': cmo.balance
})



class set_options:
    """
    xcmocean.set_options(seqin={'dye_01': cmo.matter}, regexin={'dye_01': 'dye'})
    with xcmo.set_options(seqin={'temp': cmo.matter})
    xcmo.set_options(seqin={'temp': cmo.thermal, 'salt': cmo.tempo}, divin={'temp': cmo.delta})
    """
    def __init__(self, regexin=None, seqin=None, divin=None):
        # new regexin can be input by itself
        if regexin is not None:
            self.oldregex = {}
            for vartype, pattern in regexin.items():
                if vartype in REGEX:
                    self.oldregex[vartype] = REGEX[vartype]
                else:
                    self.oldregex[vartype] = vartype
            self._apply_update_regex(regexin)
            
        # new seqin can't be input without corresponding regexin
        if seqin is not None:
            self.oldseq = {}
            for vartype, pattern in seqin.items():
                if vartype in SEQ:
                    self.oldseq[vartype] = SEQ[vartype]
                else:
                    words = 'cannot add new vartype of colormap without regex to determine vartype'
                    assert (vartype in REGEX) or (regexin is not None and vartype in regexin), words
                    self.oldseq[vartype] = vartype
            self._apply_update_seq(seqin)
            
        # new divin can't be input without corresponding regexin
        if divin is not None:
            self.olddiv = {}
            for vartype, pattern in divin.items():
                if vartype in DIV:
                    self.olddiv[vartype] = DIV[vartype]
                else:
                    words = 'cannot add new vartype of colormap without regex to determine vartype'
                    assert (vartype in REGEX) or (vartype in regexin), words
                    self.olddiv[vartype] = vartype
            self._apply_update_div(divin)

    def _apply_update_regex(self, options_dict):
        REGEX.update(options_dict)

    def _apply_update_seq(self, options_dict):
        SEQ.update(options_dict)

    def _apply_update_div(self, options_dict):
        DIV.update(options_dict)

    def __enter__(self):
        return

    def __exit__(self, type, value, traceback):
        self._apply_update_regex(self.oldregex)
        self._apply_update_seq(self.oldseq)
        self._apply_update_div(self.olddiv)
