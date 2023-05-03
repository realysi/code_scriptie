folder = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/20220202/'; 
cd(folder);

filenames = { dir('*.mat').name };

for i=1:5 %length(folder)
    fprintf('%d\n',i);
    file = filenames{i};
    load([folder,file])
    writetable(Calls, [folder,file])
end


'artis_23_audio1_2021-09-16_21-28-30_(9) 2022-12-14  1_37 AM.mat'