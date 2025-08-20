from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from config.database import DataBaseConfig


class BaseRepository(ABC):

    def __init__(self):
        self.db = DataBaseConfig()

    def execute_query(self, query: str, params: tuple = ()) -> Any:
        try:
            if params:
                self.db.get_cursor().execute(query, params)
            else:
                self.db.get_cursor().execute(query)

            if query.strip().upper().startswith("SELECT"):
                return self.db.get_cursor().fetchall()
            
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            return False
        
    def execute_query_one(self, query: str, params: tuple = None) -> Optional[tuple]:
        try:
            if params:
                self.db.get_cursor().execute(query, params)
            else:
                self.db.get_cursor().execute(query)

            return self.db.get_cursor().fetchone()
        
        except Exception as e:
            self.db.rollback()
            return None
        

    @abstractmethod
    def create(self, entity: Any) -> bool:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Optional[Any]:
        pass

    @abstractmethod
    def find_all(self) -> List[Any]:
        pass

    @abstractmethod
    def update(self, entity: Any) -> bool:
        pass

    
    def delete(self, entity_id: int) -> bool:
        pass