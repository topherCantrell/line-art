import time

class CornerCursor:
    
    def __init__(self,artist,lines,xo,yo,co,is_cw):
        self._artist = artist
        self._lines = lines
        self._xo = xo
        self._yo = yo
        self._co = co
        self._is_cw = is_cw        
        self._has_next = True
        if is_cw:
            self._po = 0
            self._index_offset = 1
        else:
            self._po = len(lines)-1
            self._index_offset = -1
        
    def has_more_to_draw(self):
        return self._has_next
        
    def draw_next(self):
        if self._is_cw:
            p0 = self._lines[self._po][0]
            p1 = self._lines[self._po][1]
        else:
            p1 = self._lines[self._po][0]
            p0 = self._lines[self._po][1]
        self._artist._lines.append((self._xo+p0[0],self._yo+p0[1],self._xo+p1[0],self._yo+p1[1]))
        self._artist._hardware.draw_line(self._xo+p0[0],self._yo+p0[1],self._xo+p1[0],self._yo+p1[1],self._co)
        self._po += self._index_offset
        if self._po<0 or self._po>=len(self._lines):
            self._has_next = False   
            
class LineArt:
    
    def __init__(self,hardware,configs):
        self._hardware = hardware        
        self._configs = configs
        
        self._lines = []
        
    def _get_line_defs(self,size,div):    
        corner_lines = {
            'A' : [],
            'B' : [],
            'C' : [],
            'D' : []
            }    
        for i in range(div):
                v = int(i*size/div)        
                corner_lines['A'].append([[0,size-v],[v,0]])        
                corner_lines['B'].append([[v,0],[size,v]])        
                corner_lines['C'].append([[size,v],[size-v,size]])        
                corner_lines['D'].append([[size-v,size],[0,size-v]])
        corner_lines['A'].append([[0,0],[size,0]])        
        corner_lines['B'].append([[size,0],[size,size]])        
        corner_lines['C'].append([[size,size],[0,size]])        
        corner_lines['D'].append([[0,size],[0,0]])
        return corner_lines
        
    def set_color(self,num,value):
        self._hardware.set_color(num,value)
    
    def pause(self,num_seconds):
        self._hardware.pause(num_seconds)
    
    def clear(self,strategy=None):
        if not strategy:
            self._hardware.clear()
        elif strategy=='UNDO':
            for x in range(len(self._lines)-1,-1,-1):
                un = self._lines[x]
                self._hardware.draw_line(un[0],un[1],un[2],un[3],0)
            self._lines = []
        else:
            raise Exception('Unknown clear strategy: '+strategy)
    
    def change_config(self,config_name):
        self._cfg = self._configs[config_name]
        self._dfs = self._get_line_defs(self._cfg['size'],self._cfg['div'])
        self._sections = self._cfg['sections']
        self._xofs = self._cfg['xofs']
        self._yofs = self._cfg['yofs']
        
    def draw(self,corners):
        corners = corners.split('+')
        cur = []
        for cor in corners:
            quad = int(cor[0])
            corn = cor[1]
            cw = True
            if corn.upper() != corn:
                cw = False
                corn = corn.upper()
            if len(cor)>2:
                co = int(cor[3:])
                self._last_color = co
            cur.append(CornerCursor(self,
                                    self._dfs[corn],
                                    self._xofs+self._sections[quad][0],
                                    self._yofs+self._sections[quad][1],
                                    self._last_color,
                                    cw))                    
        changes = True
        while changes:
            changes = False
            for c in cur:
                if c.has_more_to_draw():
                    c.draw_next()
                    changes = True      
    
    def decode_cmd(self,cmd):
        cmd = cmd.upper()
        if cmd.startswith('COLOR '):
            cmd = cmd[6:]
            pcs = cmd.split('=')            
            self.set_color(int(pcs[0].strip()),int(pcs[1].strip(),16))
        elif cmd.startswith('CONFIG '):
            self.change_config(cmd[7:].strip())
        elif cmd.startswith('SLEEP '):
            cmd = cmd[6:]
            self.pause(int(cmd.strip()))
        elif cmd == 'CLEAR':
            self.clear()
        elif cmd.startswith('CLEAR '):
            self.clear(cmd[6:].strip())
        elif cmd.startswith('DRAW '):
            cmd = cmd[5:].replace(' ','')            
            self.draw(cmd)                       
        else:
            raise Exception('Unknown command: '+cmd)
        
    def run_commands(self,cmds):
        for cmd in cmds:
            self.decode_cmd(cmd)