from code.agouti.filter import data_agouti

deployments_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/deployments.csv'
media_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/media.csv'
observations_csv = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Flevopark/observations.csv'

def main():
    data_agouti(observations_csv, media_csv, deployments_csv, 'flevopark')

if __name__ == '__main__':
    main()