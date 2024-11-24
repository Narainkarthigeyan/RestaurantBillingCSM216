CREATE DATABASE  IF NOT EXISTS `login` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `login`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: login
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `time` datetime NOT NULL,
  `bill_number` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`bill_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES ('2024-11-16 11:50:26',1261,160.00),('2024-11-16 12:23:38',1339,1580.00),('2024-11-16 12:20:06',1712,1290.00),('2024-11-16 12:43:20',1756,300.00),('2024-11-12 16:37:36',1915,430.00),('2024-11-16 12:43:38',2227,360.00),('2024-11-12 18:15:38',2533,80.00),('2024-11-13 10:09:32',2685,290.00),('2024-11-16 12:24:57',3090,1120.00),('2024-11-16 12:42:33',3128,3600.00),('2024-11-12 17:46:23',3569,480.00),('2024-11-19 20:37:45',3645,690.00),('2024-11-21 12:06:51',3670,920.00),('2024-11-16 12:40:40',4132,3500.00),('2024-11-18 11:22:25',4135,420.00),('2024-11-13 10:09:57',4171,420.00),('2024-11-16 12:29:25',4228,4710.00),('2024-11-18 11:22:52',4323,420.00),('2024-11-16 12:35:39',4690,5500.00),('2024-11-16 12:27:09',4846,140.00),('2024-11-16 12:34:24',6298,2080.00),('2024-11-16 12:25:20',6720,700.00),('2024-11-18 11:07:07',6895,1380.00),('2024-11-19 21:54:06',6935,450.00),('2024-11-18 11:26:17',7201,420.00),('2024-11-16 12:37:38',7379,3400.00),('2024-11-18 11:31:42',7502,1800.00),('2024-11-18 11:27:29',7550,150.00),('2024-11-19 22:50:47',7622,1390.00),('2024-11-12 18:28:21',8501,240.00),('2024-11-18 11:26:59',8637,280.00),('2024-11-18 11:30:44',9437,385.00),('2024-11-16 12:26:29',9445,140.00),('2024-11-17 15:09:58',9576,260.00),('2024-11-18 12:31:09',9769,150.00);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Name` varchar(100) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Mobile` bigint DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Role` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('Narain',19,9342462868,'Tirupur','Cashier'),('Mani',35,9874563210,'Thanjavur','Cashier'),('Raja',35,9874432100,'Tirupur','Waiter'),('Robert',27,9632587410,'Thoothukudi','Waiter'),('Ram',23,9864421222,'Odisha','Waiter'),('Vijay',28,6541239877,'Odisha','Chef'),('KSI',27,9874442100,'Ohio','Cleaner'),('Rangan',36,6541239899,'Africa','Cleaner'),('Aravindh',35,6897456320,'Madurai','Chef'),('David Billa',32,9874563222,'Chennai','Chef'),('Rajesh',26,7456891233,'Vellore','Driver'),('Abdul',20,7845123699,'Coimbatore','Waiter'),('Yashwanth ',19,9999999999,'Bhavani','Student');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `ItemNo` int NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(50) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `V_NV` char(2) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`ItemNo`)
) ENGINE=InnoDB AUTO_INCREMENT=1018 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1000,'Chicken Biriyani','Chicken','NV',140),(1001,'Dosa','Tiffin','V',40),(1002,'Idli','Tiffin','V',30),(1003,'Chicken Pallipalayam','Starters','NV',180),(1004,'Japan Chicken','Starters','NV',210),(1005,'Butter Naan','Rotti','V',30),(1006,'Chicken Dynamite','Starters','NV',180),(1007,'Chicken Cinthamani','Starters','NV',180),(1008,'Panner Butter Masala','Gravy','V',110),(1009,'Pepper Chicken Gravy','Gravy','NV',130),(1010,'Chicken Hot pepper','Starters','NV',180),(1011,'Momos','Starters','NV',100),(1012,'Chicken Alfam','Chicken','NV',180),(1013,'Plate Shawarma','Chicken','NV',180),(1014,'Mutton Chukka','Starters','NV',220),(1015,'Parotta','Tiffin','V',15),(1016,'Panner Tikka','Gravy','V',130),(1017,'Butter Chicken Gravy','Gravy','NV',190);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regdetails`
--

DROP TABLE IF EXISTS `regdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regdetails` (
  `Name` varchar(50) DEFAULT NULL,
  `Username` varchar(50) NOT NULL,
  `Mail` varchar(100) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `ConfirmPassword` varchar(50) DEFAULT NULL,
  `MobileNumber` bigint DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regdetails`
--

LOCK TABLES `regdetails` WRITE;
/*!40000 ALTER TABLE `regdetails` DISABLE KEYS */;
INSERT INTO `regdetails` VALUES ('Admin','admin','admin@greenwaves.in','123','123',9843063900),('dakshin','d123','d123@gmail.com','123','123',1234567890),('Employee1','emp1','emp1@greenwaves.in','123','123',9843063900),('Narain Karthigeyan','narain123','narain@gmail.com','narain@123','narain@123',9342462868),('Narain','narain2580','narainkarthi03@gmail.com','123','123',9342462868),('Ashwin','Realtoxic007','failgamergaming@gmail.com','niggabalagi','niggabalagi',7397164376),('Sekar ','sekarnigg123','shaker123@gmail.com','abc123','abc123',7894561230),('Shubhan','shubhan123','itzshubhan@gmail.com','shubhan123','shubhan123',9042691280),('Srikanth','srikanth123','srikanth123@gmail.com','sk123','sk123',9876543210),('yugi','yugig124','yugi@gmail.com','pass','pass',9244924648);
/*!40000 ALTER TABLE `regdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `udetails`
--

DROP TABLE IF EXISTS `udetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `udetails` (
  `Username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `udetails`
--

LOCK TABLES `udetails` WRITE;
/*!40000 ALTER TABLE `udetails` DISABLE KEYS */;
INSERT INTO `udetails` VALUES ('Username','Password'),('Username','Password'),('Username','Password'),('Username','Password'),('Username','Password'),('Username','Password'),('srikanth123','sk123'),('srikanth123','sk123546464'),('srikanth123','sk123546464'),('Username','Password');
/*!40000 ALTER TABLE `udetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24 11:18:17
