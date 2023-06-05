folder_path = '/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/20220202/'; 
files = dir(fullfile(folder_path, '*.mat'));
for i = 1:length(files)
    file_path = fullfile(folder_path, files(i).name); % create the full file path
    try
        load(file_path);
        fprintf("Succesfull loaded file: %s\n", file_path);
        csv_file_path = strrep(file_path, '.mat', '.csv');
        fprintf("Becomes: %s\n", csv_file_path);
        writetable(Calls, csv_file_path);
    catch
        fprintf("Error loading file: %s\n", file_path);
        continue
    end
end



    

