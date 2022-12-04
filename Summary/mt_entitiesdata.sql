-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 28, 2021 at 09:16 AM
-- Server version: 5.7.35
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `demomrat_mrattestai_staging`
--

-- --------------------------------------------------------

--
-- Table structure for table `mt_entitiesdata`
--

CREATE TABLE `mt_entitiesdata` (
  `PK_EID` int(11) NOT NULL,
  `ORG` text NOT NULL,
  `DATE` text NOT NULL,
  `PROVIDER` text NOT NULL,
  `TITLE` text NOT NULL,
  `PGRANGE` text NOT NULL,
  `is_leaf` tinyint(1) NOT NULL DEFAULT '0',
  `fk_page_id` int(11) NOT NULL,
  `fk_case_id` int(11) NOT NULL,
  `visibility` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mt_entitiesdata`
--

INSERT INTO `mt_entitiesdata` (`PK_EID`, `ORG`, `DATE`, `PROVIDER`, `TITLE`, `PGRANGE`, `is_leaf`, `fk_page_id`, `fk_case_id`, `visibility`) VALUES
(3, '', '9/6/2019', 'Karaba,RN', 'ED Depart Summary', '1', 0, 1, 299, 1),
(4, '', '02/14/2020', 'Port, MD, Robtert S, Tseng,DO,I-Wen', 'Computed Tomography', '10', 0, 2, 299, 1),
(5, 'AMERICARE AMBULANCE', '01-06-2013', '', 'PATIENT CARE RECORD', '1', 0, 1, 304, 1),
(6, 'AMERICARE AMBULANCE', '31-08-2014', 'Kassan, Rod M MD', 'PATIENT CARE RECORD', '2', 0, 2, 304, 1),
(7, 'Cembs-Sinai Medical center', '04/06/2012', 'Azarbal, Babak, MD', 'Admission Information', '10', 0, 10, 305, 1),
(8, '', '04/06/2012', 'Dohad, Suhail, MD', '', '', 0, 11, 305, 1),
(9, '', '', 'AZARBAL, BABAK [6295]', '', '', 0, 12, 305, 1),
(10, 'CedarS\'Sinai medical Center', '04/06/2012', '', '', '13', 0, 13, 305, 1),
(11, 'CedarS\'Sinai medical Center', '04/07/2012', 'Lutsky, Zachary H, MD', 'ED Notes', '14-16', 0, 14, 304, 1),
(13, '', '05/22/2019, 05/29/2019', '', '', '', 0, 2, 300, 1),
(14, 'CedarS\'Sinai medical Center', '04/06/2012', 'Al-Jiboury, Hala, MD', '', '', 0, 22, 305, 1),
(15, '', '', '', 'DISCHARGE INFORMATION', '', 0, 3, 299, 1),
(16, 'Adventist Health Tehachapi Valley', '', '', '', '', 0, 4, 299, 1),
(17, 'Adventist Health Tehachapi Valley', '09/06/2019', 'Tseng, DO, l-Wen', '', '6', 0, 6, 299, 1),
(18, '', '', 'PROVIDER', '', '', 0, 3, 300, 1),
(19, 'test2', 'test1', 'test', '', '', 0, 10, 300, 1),
(20, '', '', '', '', '18-20', 0, 18, 304, 1),
(25, '', '02/14/2019', 'Andrea Brandt', 'Timeline Report', '4-8', 0, 4, 304, 1),
(26, 'test', '01/04/2019', 'PROVIDER', '', '18-20', 0, 1, 309, 1),
(27, '', '01/15/2018', 'PROVIDER', 'Progress Report', '1-2', 0, 2, 310, 1),
(29, '', '04/06/2012', 'Dohad, Suhail, MD', 'Admission Information', '11', 0, 10, 304, 1),
(30, 'ORG', 'October 20,20171', 'PROVIDER', 'SOAP Notes', '1-2', 0, 1, 308, 1),
(31, 'CedarS\'Sinai medical Center', '04/06/2019', 'Lutsky, Zachary H, MD', 'Babak, MD', '1-2', 0, 15, 315, 1),
(33, 'test', '04/13/2012', 'test', 'H&P (continued)', '1-2', 0, 15, 324, 1),
(34, 'CedarS\'Sinai medical Center', '04/06/2012', 'Dohad, Suhail, MD', 'Discharge Summary Discharge Summary', '10-11', 0, 10, 324, 1),
(35, 'SAINT JOHN\'S HEALTH CENTER', '02/21/2014', 'WANG,DOROTHY', 'CUMULATIVE PATIENT SUMMARY', '', 0, 1, 327, 1),
(36, 'SAINT JOHN\'S HEALTH CENTER', '02/21/2014', 'WANG,DOROTHY', 'CUMULATIVE PATIENT SUMMARY', '', 0, 2, 327, 1),
(42, 'LabCorp E-Req UCLA Health System', ' 7/10/2013', 'KASSAN, ROB M', 'SMBP-MONTANA', '1', 0, 1, 331, 1),
(43, 'Laboratory Corporation of America', '7/10/2013', 'Laboratory Corporation of America', 'ANTHEM BLUE CROSS CALIFORNIA', '2', 0, 2, 331, 1),
(44, '', '01/01/2021', 'john smithhhhh', 'Patient Details', 'john smithhhhh Johnsonnn', 0, 1, 347, 1),
(45, 'Steve Smithhh johnsonn', '02/01/2020', 'Steve Smithhh', 'Pateient detailssss', '2', 0, 2, 347, 1),
(46, 'Saint John\'s Health Center', '06/01/2013', 'Seth, Sanjeev K, MD', '', '1', 0, 1, 329, 1),
(47, '', '10/12/2017', 'Grossman, Brian Maxwell', 'Lab Report', '4', 0, 4, 332, 1),
(48, 'Mayo Medical Laboratories', '24/04/2019', 'Steven J. Soldin', 'demo', '3', 0, 1, 332, 1),
(50, 'UCLA Health ', '11/13/2014', 'Jakun W. Ing, MD', 'Your Provider For Today\'S Visit', '1', 0, 1, 388, 1),
(51, 'UCLA Health', '11/13/2014', 'Jakun W. Ing, MD', 'Consults Info', '2', 0, 2, 388, 1),
(52, 'UCLA Health', '11/24/2014', 'Ing, Jakun W., MD', 'Patient Information', '3', 0, 3, 388, 1),
(53, 'Apex Chiropractic', '01/03/2018', 'Dr. Shane Kurth', 'Chart Notes', '1', 0, 1, 397, 1),
(54, '', '01/16/2018', 'Dr. Shane Kurth', 'Chart Notes', '3', 0, 3, 397, 1),
(55, 'Apex Chiropractic', '01/10/2018', 'Dr. Shane Kurth', 'Chart Notes', '2', 0, 2, 397, 1),
(56, 'Apex Chiropractic', '01/22/2018', 'Dr. Shane Kurtl', 'Chart Notes', '4', 0, 4, 397, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mt_entitiesdata`
--
ALTER TABLE `mt_entitiesdata`
  ADD PRIMARY KEY (`PK_EID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mt_entitiesdata`
--
ALTER TABLE `mt_entitiesdata`
  MODIFY `PK_EID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
