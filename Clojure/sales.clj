(use 'clojure.java.io)
(require '[clojure.string :as str])
(def customersMap (sorted-map))

(with-open [rdr (reader "cust.txt")]						; read customer data
	(doseq [line (line-seq rdr)]
	(def customers (clojure.string/split line #"\|"))
	(def id (str/trim (get customers 0)))
	(def custName (str/trim (get customers 1)))
	(def address (str/trim (get customers 2)))
	(def phoneNumber (str/trim (get customers 3)))
	
	(def temp {id {:Name custName,:Address address,:PhoneNumber phoneNumber}})
	
	(def customersMap (merge-with + customersMap temp))
	))

(def productsMap (sorted-map))	
(with-open [rdr (reader "prod.txt")]				; read product data
	(doseq [line (line-seq rdr)]
	(def products (clojure.string/split line #"\|"))
	(def id (str/trim (get products 0)))
	(def product (str/trim (get products 1)))
	(def price (str/trim (get products 2)))
	(def temp {id {:Product product,:Price price}})
	(def productsMap (merge-with + productsMap temp))
	
	))
	
(def salesMap (sorted-map))
(with-open [rdr (reader "sales.txt")]				; read sales data
	(doseq [line (line-seq rdr)]
	(def sales (clojure.string/split line #"\|"))
	(def id (str/trim (get sales 0)))
	(def customerId (str/trim (get sales 1)))
	(def productId (str/trim (get sales 2)))
	(def noOfItems (str/trim (get sales 3)))
	(def temp {id {:CustomerId customerId,:ProductId productId,:NoOfItems noOfItems}})
	(def salesMap (merge-with + salesMap temp))
))

(defn viewCustomerTable[]							; view customer table
	(println)
	(doseq [[k v] customersMap]
	(def Name (get-in v [:Name]))
	(def Address (get-in v [:Address]))
	(def PhoneNumber (get-in v [:PhoneNumber]))
	(println (str k ":[\"" Name "\" \"" Address "\" \"" PhoneNumber "\"]"))
	)
)

(defn viewProductTable[]
	(println)
	(doseq [[k v] productsMap]
	(def Product (get-in v [:Product]))
	(def Price (get-in v [:Price]))
	(println (str k ":[\"" Product "\" \"" Price "\"]"))
	)
)

(defn viewSalesTable[]
	(println)
	(doseq [[k v] salesMap]
	
	(def custId (get-in v [:CustomerId]))
	(def customer (get customersMap custId))
	(def custName (get-in customer [:Name]))
	
	(def prodId (get-in v [:ProductId]))
	(def product (get productsMap prodId))
	(def prodName (get-in product [:Product]))
	
	(def noOfItems (get-in v [:NoOfItems]))
	
	(println (str k ":[\"" custName "\" \"" prodName "\" \"" noOfItems "\"]"))
	
	)
)



(defn totalSalesForCustomer[]
(def ifStatus "no")
	(def totalAmount 0.0)
	(while (= ifStatus "no")
	(println "Enter customer name to get his sale amount : ")
	(def custName (read-line))
	(doseq [[k v] customersMap]
	(def cName (get-in v [:Name]))
	(if (.equalsIgnoreCase cName custName)
		(do(def cId k)
		(def custPrintName cName)
		(def ifStatus "yes")
		(doseq [[k v] salesMap]
		(def custId (get-in v [:CustomerId]))
		(def noOfItems (get-in v [:NoOfItems]))
		(if (= cId custId)
			(do 
			(def prodId (get-in v [:ProductId]))
			(def product (get productsMap prodId))
			(def price (get-in product [:Price]))
			(def amount (* (Float/parseFloat noOfItems) (Float/parseFloat price)))
			
			(def totalAmount (+ (float amount) (float totalAmount)))
			;(def tAmount (with-precision 2 totalAmount))
			(def tAmount (format "%.2f" totalAmount))
			
			)
		)
		)
		)
		
		
	)
	)
	(println)
	(if (= ifStatus "no")
	(do
	(println "You have entered an invalid name")
	)
	(do(println (str  custPrintName ": $" tAmount)))
	)
	)
)



(defn totalItemSoldCount[]
(def ifStatus1 "no")
(def totalCount 0)
(while (= ifStatus1 "no")
(println "Enter product name to get it's sale count : ")
(def prod (read-line))
(doseq [[k v] productsMap]
(def pName (get-in v [:Product]))
(if (.equalsIgnoreCase prod pName)
	(do
	(def ifStatus1 "yes")
	(def pId k)
	(doseq [[k v] salesMap]
	(def prodId (get-in v [:ProductId]))
	(if (= pId prodId)
	(do 
	(def countI (get-in v [:NoOfItems]))
	(def totalCount (+ (Integer/parseInt countI) totalCount))
	)
	)
	)
	)
)
)
(println)
	(if (= ifStatus1 "no")
	(do
	(println "You have entered an invalid product")
	)
	(do(println (str (str/capitalize prod) ":" totalCount)))
	)
	)
)
	
(defn intro[]
	(def option "0")
	(while(not= option "6")
	(println "\n*** Sales Menu ***")
	(println "------------------\n")
	(println "1. Display Customer Table\n2. Display Product Table\n3. Display Sales Table\n4. Total Sales for Customer\n5. Total Count for Product\n6. Exit\n")
	(println "Enter an option?")
	(def option (read-line))
	(case option "1" (viewCustomerTable)
	"2" (viewProductTable)
	"3" (viewSalesTable)
	"4" (totalSalesForCustomer)
	"5" (totalItemSoldCount)
	"6" ((println "Good Bye")
		(def option=6)
		(System/exit 0))
		
		(println "You have entered an invalid option"))
	)
)
(intro)	
	
	