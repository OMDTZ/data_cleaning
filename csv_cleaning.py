import sys, os
import csv

def cleandict(infile, outfile):
    dictreader = csv.DictReader(open(infile))
    of = open(outfile, 'w')
    writer = csv.DictWriter(of, fieldnames = dictreader.fieldnames)
    writer.writeheader()
    for row in dictreader:
        newrow = row
        try:
            newrow['energy_source'] = row['energy_source'].replace(
                'grid_LUKU', 'electricity')
            newrow['mill_type'] = row['mill_type'].replace(
                'rolling', 'roller').replace(
                'rice_grinding_machine', 'rice_milling_machine').replace(
                'maize_germ_extractor', 'dehuller')
            if(newrow['mill_type'] == 'hammer' or
                    newrow['mill_type'] == 'rice_milling_machine'):
                newrow['Packaging_flour_fortified'] = 'no'
            if not ('wheat' in newrow['commodity_milled'].lower() or
                    'maize' in newrow['commodity_milled'].lower()):
                newrow['Packaging_flour_fortified'] = 'no'

        except:
            print('not found')
        writer.writerow(newrow)

if __name__ == "__main__":
    indir = sys.argv[1]
    filelist = os.listdir(indir)
    outdir = os.path.join(indir,'CLEANED')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for filename in filelist:
        infile = os.path.join(indir, filename)
        (filepath, ext) = os.path.splitext(filename)
        outfile = os.path.join(outdir,filename)
        if ext == '.csv':
            try:
                cleandict(infile, outfile)
            except Exception as e:
                print('this file is fucked up')
                print(filename)
                print(e)

    
