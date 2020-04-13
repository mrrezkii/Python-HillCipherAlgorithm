-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2020 at 07:57 AM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 7.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tubes_kriptografi`
--

-- --------------------------------------------------------

--
-- Table structure for table `dekripsi`
--

CREATE TABLE `dekripsi` (
  `id_dekripsi` int(12) NOT NULL,
  `kata_awal_de` varchar(20) NOT NULL,
  `hasil_dekripsi` varchar(20) NOT NULL,
  `tanggal` datetime NOT NULL,
  `status_id` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `enkripsi`
--

CREATE TABLE `enkripsi` (
  `id_enkripsi` int(12) NOT NULL,
  `kata_awal_en` varchar(20) NOT NULL,
  `hasil_enkripsi` varchar(20) NOT NULL,
  `tanggal` datetime NOT NULL,
  `status_id` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id_status` int(12) NOT NULL,
  `keterangan` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id_status`, `keterangan`) VALUES
(1, 'Enkripsi'),
(2, 'Dekripsi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dekripsi`
--
ALTER TABLE `dekripsi`
  ADD PRIMARY KEY (`id_dekripsi`),
  ADD KEY `status_id` (`status_id`);

--
-- Indexes for table `enkripsi`
--
ALTER TABLE `enkripsi`
  ADD PRIMARY KEY (`id_enkripsi`),
  ADD KEY `status_id` (`status_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id_status`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dekripsi`
--
ALTER TABLE `dekripsi`
  MODIFY `id_dekripsi` int(12) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `enkripsi`
--
ALTER TABLE `enkripsi`
  MODIFY `id_enkripsi` int(12) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
