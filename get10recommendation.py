# Prediksi rating untuk user_id = 1 dan anime_id = 101
import pickle
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split, cross_validate

user_id = 1
anime_id = 101
predicted_rating = model.predict(user_id, anime_id).est
print(f"Predicted rating for user {user_id} and anime {anime_id}: {predicted_rating}")


def get_top_n_recommendations(user_id, model, trainset, n=10):
    all_items = set(trainset.all_items())
    anime_id_map = {trainset.to_raw_iid(i): i for i in all_items}
    seen_items = {j for (j, _) in trainset.ur[trainset.to_inner_uid(user_id)]}
    unseen_items = all_items - seen_items

    predictions = [
        (anime_id_map[item_id], model.predict(user_id, trainset.to_raw_iid(item_id)).est)
        for item_id in unseen_items
    ]
    top_n = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]
    return [{"anime_id": anime_id, "predicted_rating": rating} for anime_id, rating in top_n]

# Contoh: rekomendasi untuk user_id = 1
top_10_anime = get_top_n_recommendations(1, model, trainset)
print("Top 10 Recommendations:")
for rec in top_10_anime:
    print(rec)
