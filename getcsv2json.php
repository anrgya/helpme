<?php

function csvToJson($csvUrl) {
    $csvData = [];

    if (($handle = fopen($csvUrl, 'r')) !== false) {
        // Menghapus karakter BOM jika ada
        $firstLine = fgets($handle);
        $firstLine = preg_replace('/^\xEF\xBB\xBF/', '', $firstLine);
        
        // Membaca kembali baris pertama tanpa BOM
        $csvData[] = str_getcsv($firstLine);
        
        while (($row = fgetcsv($handle)) !== false) {
            $csvData[] = $row;
        }
        fclose($handle);
    }

    // Ambil baris pertama sebagai header
    $headers = array_shift($csvData);

    $jsonArray = [];

    // Gabungkan header dengan baris-baris berikutnya
    foreach ($csvData as $row) {
        $jsonArrayItem = [];
        for ($i = 0; $i < count($headers); $i++) {
            $jsonArrayItem[$headers[$i]] = $row[$i] ?? null;
        }
        $jsonArray[] = $jsonArrayItem;
    }

    return json_encode($jsonArray);
}

$csvUrl = 'datapribadi.csv'; // Menggunakan file CSV lokal
$jsonData = csvToJson($csvUrl);

// Set header ke JSON
header('Content-Type: application/json');

// Output data JSON
echo $jsonData;
?>
