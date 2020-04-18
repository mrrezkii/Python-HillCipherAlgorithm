-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2020 at 03:34 AM
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
  `tanggal` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dekripsi`
--

INSERT INTO `dekripsi` (`id_dekripsi`, `kata_awal_de`, `hasil_dekripsi`, `tanggal`) VALUES
(1, 'POH', 'ACT', '2020-04-18 08:24:13'),
(2, 'POH', 'ACT', '2020-04-18 08:31:21');

-- --------------------------------------------------------

--
-- Table structure for table `enkripsi`
--

CREATE TABLE `enkripsi` (
  `id_enkripsi` int(12) NOT NULL,
  `kata_awal_en` varchar(20) NOT NULL,
  `hasil_enkripsi` varchar(20) NOT NULL,
  `tanggal` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `enkripsi`
--

INSERT INTO `enkripsi` (`id_enkripsi`, `kata_awal_en`, `hasil_enkripsi`, `tanggal`) VALUES
(1, 'ACT', 'ACT', '0000-00-00 00:00:00'),
(2, 'ACT', 'ACT', '2020-04-18 08:17:20'),
(3, 'ACT', 'ACT', '2020-04-18 08:17:55'),
(4, 'ACT', 'ACT', '2020-04-18 08:18:15'),
(5, 'ACT', 'POH', '2020-04-18 08:20:01'),
(6, 'DAD', 'VRB', '2020-04-18 08:24:41'),
(7, 'ACT', 'POH', '2020-04-18 08:31:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dekripsi`
--
ALTER TABLE `dekripsi`
  ADD PRIMARY KEY (`id_dekripsi`);

--
-- Indexes for table `enkripsi`
--
ALTER TABLE `enkripsi`
  ADD PRIMARY KEY (`id_enkripsi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dekripsi`
--
ALTER TABLE `dekripsi`
  MODIFY `id_dekripsi` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `enkripsi`
--
ALTER TABLE `enkripsi`
  MODIFY `id_enkripsi` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
