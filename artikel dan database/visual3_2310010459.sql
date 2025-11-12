-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 12, 2025 at 09:40 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visual3_2310010459`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama_lengkap` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `role` enum('admin','staff') DEFAULT 'staff',
  `tanggal_dibuat` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `username`, `password`, `nama_lengkap`, `email`, `role`, `tanggal_dibuat`) VALUES
(1, 'lana', '123456', 'Administrator Satu', 'admin1@example.com', 'admin', '2025-11-05 13:13:47'),
(2, 'aldi ayam', '123456', 'Administrator Dua', 'admin2@example.com', 'staff', '2025-11-05 13:13:47'),
(3, 'galuh', '123456', 'Administrator Tiga', 'admin3@example.com', 'staff', '2025-11-05 13:13:47'),
(4, 'nabil jaky', '123456', 'Administrator Empat', 'admin4@example.com', 'admin', '2025-11-05 13:13:47'),
(5, 'azmi', '123456', 'Administrator Lima', 'admin5@example.com', 'staff', '2025-11-05 13:13:47'),
(14, 'sean', '14455', 'syarif', 'syarif@gmail.com', 'admin', '2025-11-12 05:46:53');

-- --------------------------------------------------------

--
-- Table structure for table `keluarga`
--

CREATE TABLE `keluarga` (
  `id_keluarga` int(11) NOT NULL,
  `nama_kepala_keluarga` varchar(100) NOT NULL,
  `alamat` varchar(150) DEFAULT NULL,
  `jumlah_anggota` int(11) DEFAULT NULL,
  `status_ekonomi` enum('sejahtera bawah','sejahtera menengah','sejahtera atas') DEFAULT 'sejahtera bawah',
  `id_usaha` int(11) DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keluarga`
--

INSERT INTO `keluarga` (`id_keluarga`, `nama_kepala_keluarga`, `alamat`, `jumlah_anggota`, `status_ekonomi`, `id_usaha`, `dibuat_oleh`) VALUES
(5, 'Budi Santoso', 'Jl. Ahmad Yani Km 5, Banjarmasin', 4, 'sejahtera menengah', 27, 1),
(6, 'Siti Maemunah', 'Jl. Panglima Batur, Banjarbaru', 5, 'sejahtera atas', 28, 2),
(7, 'Rahmat Hidayat', 'Jl. Merdeka, Martapura', 3, 'sejahtera bawah', 29, 3),
(8, 'Nur Aisyah', 'Jl. Antang Kalang, Palangkaraya', 6, 'sejahtera menengah', 30, 4),
(9, 'Hendra Gunawan', 'Jl. Veteran, Banjarmasin', 5, 'sejahtera atas', 31, 5),
(25, 'AZMI KHAIRY', 'pondok duren', 11, 'sejahtera atas', 47, 2);

-- --------------------------------------------------------

--
-- Table structure for table `kesejahteraan`
--

CREATE TABLE `kesejahteraan` (
  `id_kesejahteraan` int(11) NOT NULL,
  `id_keluarga` int(11) DEFAULT NULL,
  `tahun` year(4) DEFAULT NULL,
  `penghasilan` decimal(12,2) DEFAULT NULL,
  `pendidikan_anak` varchar(100) DEFAULT NULL,
  `status_rumah` enum('kontrak','milik sendiri') DEFAULT 'kontrak',
  `kategori_ipm` enum('rendah','menengah bawah','menengah atas','tinggi') DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kesejahteraan`
--

INSERT INTO `kesejahteraan` (`id_kesejahteraan`, `id_keluarga`, `tahun`, `penghasilan`, `pendidikan_anak`, `status_rumah`, `kategori_ipm`, `dibuat_oleh`) VALUES
(21, 5, '2025', 1000000.00, 'SMA & Diploma', 'milik sendiri', 'menengah bawah', 1),
(22, 6, '2025', 1000000.00, 'SMP & SMA', 'kontrak', 'menengah atas', 2),
(23, 7, '2024', 100000.00, 'SD & SMP', 'kontrak', 'rendah', 3),
(24, 8, '2025', 1000000.00, 'SMA', 'milik sendiri', 'menengah bawah', 4),
(25, 9, '2025', 1000000.00, 'SMA & Kuliah', 'milik sendiri', 'menengah atas', 5),
(41, 25, '2025', 1000000000.00, 'S1', 'milik sendiri', 'menengah atas', 2);

-- --------------------------------------------------------

--
-- Table structure for table `pekerja`
--

CREATE TABLE `pekerja` (
  `id_pekerja` int(11) NOT NULL,
  `nama_pekerja` varchar(100) NOT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') NOT NULL,
  `pekerjaan` varchar(100) DEFAULT NULL,
  `gaji` decimal(12,2) DEFAULT NULL,
  `id_usaha` int(11) DEFAULT NULL,
  `id_keluarga` int(11) DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pekerja`
--

INSERT INTO `pekerja` (`id_pekerja`, `nama_pekerja`, `jenis_kelamin`, `pekerjaan`, `gaji`, `id_usaha`, `id_keluarga`, `dibuat_oleh`) VALUES
(1, 'Ahmad Fauzi', 'Laki-laki', 'Operator Crusher', 3599182.00, 27, 5, 1),
(2, 'Nurul Hidayah', 'Perempuan', 'Operator Conveyor', 3496195.00, 28, 6, 2),
(3, 'Rahmad Saputra', 'Laki-laki', 'Operator Screening', 3496195.00, 29, 7, 3),
(4, 'Aisyah Putri', 'Perempuan', 'Quality Control (Lab)', 3525154.26, 30, 8, 4),
(5, 'Hendri Kurnia', 'Laki-laki', 'Mekanik Alat Berat', 3599182.00, 31, 9, 5),
(21, 'anwar', 'Laki-laki', 'mekanik alat', 49000000.00, 47, 8, 3);

-- --------------------------------------------------------

--
-- Table structure for table `pendampingan`
--

CREATE TABLE `pendampingan` (
  `id_pendampingan` int(11) NOT NULL,
  `nama_program` varchar(100) DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_selesai` date DEFAULT NULL,
  `lembaga_pendamping` varchar(100) DEFAULT NULL,
  `id_usaha` int(11) DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pendampingan`
--

INSERT INTO `pendampingan` (`id_pendampingan`, `nama_program`, `tanggal_mulai`, `tanggal_selesai`, `lembaga_pendamping`, `id_usaha`, `dibuat_oleh`) VALUES
(1, 'Pelatihan K3 Dasar Tambang', '2025-01-10', '2025-01-12', 'Disnaker Kalsel', 27, 1),
(2, 'Sertifikasi Operator Crusher', '2025-02-03', '2025-02-05', 'BLK Banjarmasin', 28, 2),
(3, 'Manajemen Mutu ISO 9001:2025', '2025-02-17', '2025-02-19', 'LSP Manajemen Mutu', 29, 3),
(4, 'Sampling & QC Batu Kapur', '2025-03-05', '2025-03-06', 'Politeknik Negeri', 30, 4),
(5, 'Perawatan Alat Berat (Basic)', '2025-03-20', '2025-03-22', 'Balai Diklat ESDM', 31, 5),
(21, 'mcu', '2025-01-01', '2025-01-23', 'Dinas Kesehatan', 47, 2);

-- --------------------------------------------------------

--
-- Table structure for table `risiko_pekerjaan`
--

CREATE TABLE `risiko_pekerjaan` (
  `id_risiko` int(11) NOT NULL,
  `id_pekerja` int(11) DEFAULT NULL,
  `jenis_risiko` varchar(150) DEFAULT NULL,
  `tingkat_risiko` enum('rendah','sedang','tinggi') DEFAULT 'sedang',
  `tindakan_pencegahan` varchar(200) DEFAULT NULL,
  `tanggal_insiden` date DEFAULT NULL,
  `dibuat_oleh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `risiko_pekerjaan`
--

INSERT INTO `risiko_pekerjaan` (`id_risiko`, `id_pekerja`, `jenis_risiko`, `tingkat_risiko`, `tindakan_pencegahan`, `tanggal_insiden`, `dibuat_oleh`) VALUES
(6, 1, 'patah tulang', 'tinggi', 'rumah sakit', '2025-11-05', 5),
(7, 2, 'bocor', 'rendah', 'wc', '2025-11-03', 2),
(8, 21, 'Makan besi', 'rendah', 'sholat', '2000-01-01', 5);

-- --------------------------------------------------------

--
-- Table structure for table `usaha_batu_kapur`
--

CREATE TABLE `usaha_batu_kapur` (
  `id_usaha` int(11) NOT NULL,
  `nama_usaha` varchar(100) NOT NULL,
  `lokasi` varchar(100) DEFAULT NULL,
  `tahun_berdiri` year(4) DEFAULT NULL,
  `jumlah_buruh` int(11) DEFAULT NULL,
  `pendapatan_bulanan` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usaha_batu_kapur`
--

INSERT INTO `usaha_batu_kapur` (`id_usaha`, `nama_usaha`, `lokasi`, `tahun_berdiri`, `jumlah_buruh`, `pendapatan_bulanan`) VALUES
(27, 'Warung Sederhana', 'Banjarmasin', '2019', 3, 7500000.00),
(28, 'CV Nusantara Tech', 'Banjarbaru', '2016', 15, 28500000.00),
(29, 'Toko Sejahtera', 'Martapura', '2018', 6, 12000000.00),
(30, 'Kopi Kalimantan', 'Palangkaraya', '2021', 8, 17500000.00),
(31, 'Bengkel Maju Jaya', 'Banjarmasin', '2015', 10, 22000000.00),
(47, 'BATU KAPUR GAMBUT', 'Jepara', '2025', 6, 89000000.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `keluarga`
--
ALTER TABLE `keluarga`
  ADD PRIMARY KEY (`id_keluarga`),
  ADD KEY `id_usaha` (`id_usaha`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indexes for table `kesejahteraan`
--
ALTER TABLE `kesejahteraan`
  ADD PRIMARY KEY (`id_kesejahteraan`),
  ADD KEY `id_keluarga` (`id_keluarga`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indexes for table `pekerja`
--
ALTER TABLE `pekerja`
  ADD PRIMARY KEY (`id_pekerja`),
  ADD KEY `id_usaha` (`id_usaha`),
  ADD KEY `id_keluarga` (`id_keluarga`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indexes for table `pendampingan`
--
ALTER TABLE `pendampingan`
  ADD PRIMARY KEY (`id_pendampingan`),
  ADD KEY `id_usaha` (`id_usaha`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indexes for table `risiko_pekerjaan`
--
ALTER TABLE `risiko_pekerjaan`
  ADD PRIMARY KEY (`id_risiko`),
  ADD KEY `id_pekerja` (`id_pekerja`),
  ADD KEY `dibuat_oleh` (`dibuat_oleh`);

--
-- Indexes for table `usaha_batu_kapur`
--
ALTER TABLE `usaha_batu_kapur`
  ADD PRIMARY KEY (`id_usaha`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `keluarga`
--
ALTER TABLE `keluarga`
  MODIFY `id_keluarga` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `kesejahteraan`
--
ALTER TABLE `kesejahteraan`
  MODIFY `id_kesejahteraan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `pekerja`
--
ALTER TABLE `pekerja`
  MODIFY `id_pekerja` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `pendampingan`
--
ALTER TABLE `pendampingan`
  MODIFY `id_pendampingan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `risiko_pekerjaan`
--
ALTER TABLE `risiko_pekerjaan`
  MODIFY `id_risiko` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `usaha_batu_kapur`
--
ALTER TABLE `usaha_batu_kapur`
  MODIFY `id_usaha` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `keluarga`
--
ALTER TABLE `keluarga`
  ADD CONSTRAINT `keluarga_ibfk_1` FOREIGN KEY (`id_usaha`) REFERENCES `usaha_batu_kapur` (`id_usaha`),
  ADD CONSTRAINT `keluarga_ibfk_2` FOREIGN KEY (`dibuat_oleh`) REFERENCES `admin` (`id_admin`);

--
-- Constraints for table `kesejahteraan`
--
ALTER TABLE `kesejahteraan`
  ADD CONSTRAINT `kesejahteraan_ibfk_1` FOREIGN KEY (`id_keluarga`) REFERENCES `keluarga` (`id_keluarga`),
  ADD CONSTRAINT `kesejahteraan_ibfk_2` FOREIGN KEY (`dibuat_oleh`) REFERENCES `admin` (`id_admin`);

--
-- Constraints for table `pekerja`
--
ALTER TABLE `pekerja`
  ADD CONSTRAINT `pekerja_ibfk_1` FOREIGN KEY (`id_usaha`) REFERENCES `usaha_batu_kapur` (`id_usaha`),
  ADD CONSTRAINT `pekerja_ibfk_2` FOREIGN KEY (`id_keluarga`) REFERENCES `keluarga` (`id_keluarga`),
  ADD CONSTRAINT `pekerja_ibfk_3` FOREIGN KEY (`dibuat_oleh`) REFERENCES `admin` (`id_admin`);

--
-- Constraints for table `pendampingan`
--
ALTER TABLE `pendampingan`
  ADD CONSTRAINT `pendampingan_ibfk_1` FOREIGN KEY (`id_usaha`) REFERENCES `usaha_batu_kapur` (`id_usaha`),
  ADD CONSTRAINT `pendampingan_ibfk_2` FOREIGN KEY (`dibuat_oleh`) REFERENCES `admin` (`id_admin`);

--
-- Constraints for table `risiko_pekerjaan`
--
ALTER TABLE `risiko_pekerjaan`
  ADD CONSTRAINT `risiko_pekerjaan_ibfk_1` FOREIGN KEY (`id_pekerja`) REFERENCES `pekerja` (`id_pekerja`),
  ADD CONSTRAINT `risiko_pekerjaan_ibfk_2` FOREIGN KEY (`dibuat_oleh`) REFERENCES `admin` (`id_admin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
