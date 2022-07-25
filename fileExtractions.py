class FileExtractions:
    def obtain_hashes_sign(self,file):
        with open(file) as f:
            lines = [x.split() for x in f.read().split("-----BEGIN PGP SIGNATURE-----") if x]
        for i in range(3):
            del lines[1][len(lines[1])-1]
        return "".join(lines[1])
