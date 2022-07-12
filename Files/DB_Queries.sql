CREATE TABLE PRODUCT
(
  ProductID INT NOT NULL,
  ProductName VARCHAR(64) NOT NULL,
  ProductPrice FLOAT NOT NULL,
  Rating FLOAT,
  About VARCHAR(100),
  DateAdded DATE,
  PRIMARY KEY (ProductID)
);

CREATE TABLE CATEGORY
(
  CategoryID INT NOT NULL,
  CategoryName VARCHAR(20) NOT NULL,
  PRIMARY KEY (CategoryID),
);

CREATE TABLE STORE
(
StoreID INT NOT NULL,
StoreName VARCHAR(40) NOT NULL,
PRIMARY KEY (StoreID),
);

CREATE TABLE USER
(
  UserID INT NOT NULL,
  Username VARCHAR(20) NOT NULL,
  UserFname VARCHAR(40) NOT NULL,
  UserLname VARCHAR(40) NOT NULL,
  Phone INT NOT NULL,
  Pass VARCHAR(16) NOT NULL,
  AddressID INT NOT NULL,
  PRIMARY KEY (UserID),
  FOREIGN KEY AddressID REFERENCES ADDRESSES(AddressID),
);

CREATE TABLE ADDRESSES
(
  AddressID INT NOT NULL,
  Addresses VARCHAR(100) NOT NULL,
  PRIMARY KEY (AddressID),
);

CREATE TABLE PROMOTION
(
  CodeID INT NOT NULL,
  PERCENT INT NOT NULL,
  PRIMARY KEY (CodeID),
);

CREATE TABLE ORDER
(
  OrderID INT NOT NULL,
  Orderdate DATE NOT NULL,
  Method VARCHAR(20) NOT NULL,
  UserID INT NOT NULL,
  AddressID INT NOT NULL,
  CodeID INT NOT NULL,
  PRIMARY KEY (OrderID),
  FOREIGN KEY (UserID) REFERENCES USER(UserID),
  FOREIGN KEY (AddressID) REFERENCES ADDRESSES(AddressID),
  FOREIGN KEY (CodeID) REFERENCES PROMOTION(CodeID),
);

CREATE TABLE REVIEW
(
  ReviewID INT NOT NULL,
  ReviewText VARCHAR(100) NOT NULL,
  UserID INT NOT NULL,
  ProductID INT NOT NULL,
  PRIMARY KEY (ReviewID),
  FOREIGN KEY UserID REFERENCES USER(UserID),
  FOREIGN KEY ProductID REFERENCES PRODUCT(PROductID),
);

CREATE TABLE PROCAT
(
  ProductID INT NOT NULL,
  CategoryID INT NOT NULL,
  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
  FOREIGN KEY CategoryID REFERENCES CATEGORY(CategoryID),
  PRIMARY KEY ProductID, CategoryID,
);

CREATE TABLE PROSTORE
(
  ProductID INT NOT NULL,
  StoreID INT NOT NULL,
  Availabilities BINARY,
  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
  FOREIGN KEY StoreID REFERENCES STORE(StoreID),
  PRIMARY KEY ProductID, StoreID,
);

CREATE TABLE PROORDER
(
  ProductID INT NOT NULL,
  OrderID INT NOT NULL,
  TotalPrice INT NOT NULL,
  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
  FOREIGN KEY OrderID REFERENCES ORDER(OrderID),
  PRIMARY KEY ProductID, OrderID,
); 



SELECT * FROM shop_store

SELECT * FROM shop_store WHERE name == %s
SELECT * FROM shop_storeproduct WHERE store_id == %s

SELECT * FROM shop_product WHERE name == %s

SELECT * FROM shop_product ORDER BY price
SELECT * FROM shop_product ORDER BY price DESC
SELECT * FROM shop_product ORDER BY rate DESC
SELECT * FROM shop_product ORDER BY date
SELECT * FROM shop_product

SELECT * FROM shop_product WHERE name == %s
SELECT * FROM shop_review WHERE product_id == %s
SELECT * FROM user_user WHERE id == %s
SELECT * FROM shop_product WHERE name == %s
SELECT * FROM shop_review WHERE product_id == %s

SELECT * FROM shop_category

SELECT * FROM shop_category WHERE name == %s
SELECT * FROM shop_productcategory WHERE category_id == %s

SELECT * FROM user_useraddress WHERE id == %s
SELECT * FROM shop_storeproduct WHERE id == %s

