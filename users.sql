-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 17, 2023 at 04:22 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `admindetails`
--

CREATE TABLE `admindetails` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admindetails`
--

INSERT INTO `admindetails` (`username`, `password`) VALUES
('admin', 'password'),
('karthik', 'qawsed');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `username` varchar(20) NOT NULL,
  `flightno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`username`, `flightno`) VALUES
('karthik', '12345'),
('karthik', '12345'),
('karthik', '12345');

--
-- Triggers `bookings`
--
DELIMITER $$
CREATE TRIGGER `update_avail` AFTER INSERT ON `bookings` FOR EACH ROW BEGIN
    UPDATE flightdetails
    SET availableseats = availableseats - 1
    WHERE flightno = NEW.flightno;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `flightdetails`
--

CREATE TABLE `flightdetails` (
  `flightno` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `start` varchar(20) NOT NULL,
  `destination` varchar(20) NOT NULL,
  `availableseats` int(11) NOT NULL DEFAULT 60
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flightdetails`
--

INSERT INTO `flightdetails` (`flightno`, `date`, `time`, `start`, `destination`, `availableseats`) VALUES
('12345', '2023-06-17', '19:30:00', 'Banglore', 'Vijaywada', 57),
('1478', '2023-06-23', '06:30:00', 'Hyderabad', 'Banglore', 60);

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `username` varchar(20) NOT NULL,
  `password` varchar(25) NOT NULL,
  `mailid` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`username`, `password`, `mailid`) VALUES
('karthik', '1q2w', 'karthik@gmail.com'),
('QAWSED', 'qawsed', 'qawsed@gmail.com'),
('username', 'password', 'username@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admindetails`
--
ALTER TABLE `admindetails`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `flightdetails`
--
ALTER TABLE `flightdetails`
  ADD PRIMARY KEY (`flightno`);

--
-- Indexes for table `userdetails`
--
ALTER TABLE `userdetails`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
