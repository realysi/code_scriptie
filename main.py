from code.check import check
from code.interface import flags
from code.run import run

folder_agouti: str = '/Users/yanickidsinga/Documents/flevopark-20230202124032'
folder_deepsqueak: str = ''

location_data: str = 'amsterdao'
name_dataset: str = 'hij'

INTERVAL_AGOUTI: int = 0
INTERVAL_DEEPSQUEAK: int = 0
INTERVAL_OVERLAP: int = 0


def main():
    #see if variables above can make this program work.
    check(path_folder_agouti=folder_agouti, path_folder_deepsqueak=folder_deepsqueak)
    #check for flags/command line arguments
    flags()
    #run program
    run()
    #print/summarize results

if __name__ == '__main__':
    main()
