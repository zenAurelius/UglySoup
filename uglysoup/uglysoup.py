
import re
import html


class UglySoup:

    def __init__(self, s="", a={}, e=0, tag_name=None):
        self.s = str(s)
        self.attr = a
        self.end = e
        self.tag = tag_name

    def find(self, req_deb, req_fin, start=0):
        found = self.s.find(req_deb, start)
        if found < 0:
            return None

        # find the tag
        tag_start = self.s.rfind("<", 0, found+1)
        m = re.search(" |>", self.s[tag_start:]).start()
        tag_name = self.s[tag_start+1: tag_start+m]
        tag_end = self.s.find(">", tag_start+1)
        full_tag = self.s[tag_start+1: tag_end]
                
        # trouver les attributs
        a = {}
        att_m = re.finditer('([^\s]+=)(\".*?\")', full_tag)
        for m in att_m:
            a[m.group(1).strip('=')] = html.unescape(m.group(2)).strip('"')

        # find the content - if ending is not found, we go to the end
        end = self.s.find(req_fin, tag_end)
        if end < 0:
            end = len(self.s)
        content = self.s[tag_end+1:end].strip()

        # return a new soup
        return UglySoup(content, a, end, tag_name)

    def findAll(self, req_deb, req_fin):
        found = []
        a = self.find(req_deb, req_fin)
        while a:
            # print(a.end)
            # print(self.s[a.end:1000])
            found.append(a)
            a = self.find(req_deb, req_fin, a.end)
        return found

    def rawFind(self, req_deb, req_fin, start=0):
        deb = self.s.find(req_deb, start)
        if deb < 0:
            return None

        fin = self.s.find(req_fin, deb)
        if fin < 0:
            return None

        return self.s[deb+len(req_deb):fin].strip()
