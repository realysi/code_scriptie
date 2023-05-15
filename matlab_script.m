folder_path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/20220202/'; 
files = dir(fullfile(folder_path, '*.mat'));
for i = 1:length(files)
    file_path = fullfile(folder_path, files(i).name); % create the full file path
    fprintf('%d/n', file_path)
    %file_contents = fileread(file_path);
    %disp(file_contents);
    % read the contents of the file
    % process the file contents as needed
end

%filenames = { dir('*.mat').name };

%{
for i=1:5 %length(folder)
    fprintf('%d\n',i);
    file = filenames{i};
    load([folder,file])
    writetable(Calls, [folder,file])
end
%}


%'artis_23_audio1_2021-09-16_21-28-30_(9) 2022-12-14  1_37 AM.mat'