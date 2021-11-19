class genbanktool:

    Filetype = ''

    # Add try exept later

    def __init__(self, file):
        try:
            if file.lower().endswith('.gp'):
                self.Filetype = 'gp'
            elif file.lower().endswith('.gb'):
                self.Filetype = 'gb'
        except:
            return "Incorrect file format"

        # Check extension
        import GenbankParser
        import Feature

    # def parser(self):


test = genbanktool('CFTR_DNA.g')
print(test)